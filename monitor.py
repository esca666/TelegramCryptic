from telethon.tl.functions.messages import GetHistoryRequest

def run(client):
    print("[*] Monitoring messages in real-time")
    group_id = input("Enter the group/channel ID: ")

    group = client.get_entity(group_id)

    print("[*] Monitoring new messages...")
    for message in client.iter_messages(group):
        print(f"New message from {message.sender_id}: {message.text}")
