import requests
from bs4 import BeautifulSoup

def find_telegram_groups():
    # Public website listing Telegram groups
    url = "https://telegramchannels.me/"  # You can change this to another source if needed
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all channels in the page
    groups = soup.find_all('div', class_='channel')

    print("[*] Found Telegram Channels:")
    for group in groups:
        name = group.find('a').get_text()
        link = group.find('a')['href']
        print(f"Group: {name} - Link: {link}")
