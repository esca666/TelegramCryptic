from telethon import TelegramClient

def get_client():
    # Prompt the user to enter their API ID and API Hash
    API_ID = input("Enter your API ID: ")
    API_HASH = input("Enter your API Hash: ")

    # Convert API_ID to integer, as Telethon expects it to be an integer
    API_ID = int(API_ID)

    client = TelegramClient('session_name', API_ID, API_HASH)
    return client
