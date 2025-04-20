from telethon.tl.functions.messages import GetHistoryRequest
from nltk.sentiment import SentimentIntensityAnalyzer

def run(client):
    print("[*] Analyzing messages")
    group_id = input("Enter the group/channel ID: ")

    group = client.get_entity(group_id)
    messages = client(GetHistoryRequest(group, limit=100))

    analyzer = SentimentIntensityAnalyzer()
    print("[*] Analyzing sentiment of last 100 messages:")
    
    for message in messages.messages:
        sentiment = analyzer.polarity_scores(message.text)
        print(f"Message: {message.text[:50]}... Sentiment: {sentiment}")
