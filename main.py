import logging
import threading
import time
from datetime import datetime

import telebot
import schedule
from schedule import repeat, every
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

import config
from models import Message

model = config.mistral_model
group_id = config.group_id
tg_api_key = config.tg_api_key
mistral_api_key = config.mistral_api_key
max_messages = config.max_messages

temperature = config.model_temperature
max_tokens = config.max_tokens

inital_prompt = config.initial_prompt
delete_time = config.delete_message_time

format = config.format

logger = logging.getLogger(__name__)
logging.basicConfig(format=format, encoding='utf-8',level=logging.INFO)

bot = telebot.TeleBot(tg_api_key)
client = MistralClient(mistral_api_key)

context = []
messages_to_delete = {}


@bot.message_handler(commands=['history'])
def restore_messages(message: telebot.types.Message):

    bot.send_message(group_id, 'Restoring messages, please wait...')
    str_dialogue = '\n'.join([f'({mess.timestamp}) {mess.user_name}: {mess.msg_text}' for mess in sorted(context, key=lambda x: x.timestamp)])
    logger.info(f'Restored dialogue: {str_dialogue}')


    messages = [ChatMessage(role="system", content=inital_prompt), ChatMessage(role='user', content=str_dialogue)]

    try:
        summary = client.chat(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        summary = bot.send_message(group_id, summary.choices[0].message.content)
        threading.Thread(target=delete_message, args=(summary.message_id, summary.chat.id)).start()
        logger.info('code')
    except Exception as e:
        logger.error(f'Error generating summary: {e}')
        bot.send_message(group_id, 'Sorry, I encountered an error while generating the summary')



@bot.message_handler(func=lambda message: True)
def main(message: telebot.types.Message):
    message_time = datetime.fromtimestamp(message.date)
    context.append(Message(timestamp=message_time, user_name=message.from_user.full_name, msg_text=message.text))

    if len(context) > max_messages:
        context.pop(0)
    

def delete_message(message_id, chat_id):
    time.sleep(60 * delete_time)
    try:
        bot.delete_message(chat_id, message_id)
    except Exception as e:
        logger.error(f"Error deleting message: {e}")

if __name__ == "__main__":
    logger.info('bot started')
    bot.infinity_polling()