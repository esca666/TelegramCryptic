from telethon import TelegramClient

API_ID = 'your_api_id'  # Replace with your Telegram API ID
API_HASH = 'your_api_hash'  # Replace with your Telegram API Hash

def get_client():
    client = TelegramClient('session_name', API_ID, API_HASH)
    return client
