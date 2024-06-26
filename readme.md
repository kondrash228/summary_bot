# Voice Summary Bot (in development)

This bot is designed to summarize group conversations in Telegram. It can transcribe voice and video messages using the Whisper model, and then generate a summary of the conversation using the Mistral AI model. The summary can be provided as text or audio using ElevenLabs text-to-speech service.

## TODO
- Implement customizable summaries that allow users to set the desired length, level of detail, and tone of the summary.
- Add a feature that enables users to filter the messages that are included in the summary based on specific criteria, such as the sender, date, or message content.
- Develop a sentiment analysis tool that can determine the overall sentiment of the group conversation and include it in the summary. 
- Create a categorization system that can automatically classify messages into predefined categories, such as questions, updates, and announcements, and present them in a structured format.
- Implement a feature that generates summaries for specific time periods, such as daily, weekly, or monthly summaries.
- Enhance the summary generation to include the content of attachments, such as documents and images, shared in the chat


## Features

- Transcribes voice and video messages using the [Whisper model](https://github.com/SYSTRAN/faster-whisper)
- Generates a summary of the conversation using the [Mistral AI model](https://mistral.ai)
- Can provide the summary as text or audio using [ElevenLabs](https://elevenlabs.io)
- Automatically deletes messages after a specified time

The bot uses a custom `Message` model to store and manage messages. The `Message` model has the following attributes:

- `timestamp`: the time when the message was sent.
- `user_name`: the name of the user who sent the message.
- `msg_text`: the text of the message.

## Setup

1. Clone the repository.
2. Install the required packages using pip:
```
pip install -r requirements.txt
```
3. Create a `config.py` file and add your credentials:
```python
mistral_model = 'your_mistral_model'
whisper_model = 'your_whisper_model'
group_id = your_group_id
tg_api_key = 'your_telegram_api_key'
mistral_api_key = 'your_mistral_api_key'
eleven_labs_api_key = 'your_eleven_labs_api_key'
eleven_labs_model = 'your_eleven_labs_model'
eleven_labs_voice = 'your_eleven_labs_voice'

temperature = your_temperature
max_tokens = your_max_tokens

inital_prompt = 'your_initial_prompt'
delete_message_time = your_delete_message_time

format = your_logging_format
```
4. Run the bot using the following command:
```
python main.py
```

## Usage

- To restore messages and generate a summary, use the `/history` command. If you want an audio summary, use `/history audio`.
- The bot will automatically transcribe voice and video messages and add them to the conversation context.
- The bot will automatically delete messages after a specified time.

## Directories

The bot will create the following directories if they don't exist:

- `{group_id}/voice`: for storing voice messages.
- `{group_id}/voice_notes`: for storing video notes.
- `{group_id}/voice_summary`: for storing audio summaries.

## Logging

The bot uses the logging module to log events. The logs are printed to the console.

## Note

The bot uses the Whisper model for transcription, the Mistral AI model for summary generation, and the ElevenLabs' text-to-speech service for audio summaries. These services may have usage limits and costs associated with them. Please refer to their respective documentation for more information.

