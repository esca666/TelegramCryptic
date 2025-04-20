from telethon.tl.functions.messages import GetFullChatRequest

def run(client):
    print("[*] Extracting members from a group/channel")
    group_id = input("Enter the group/channel ID: ")

    group = client.get_entity(group_id)
    full_chat = client(GetFullChatRequest(group.id))  # This fetches full chat info, including participants

    print(f"[*] Found {len(full_chat.participants)} members:")
    for user in full_chat.participants:
        print(f"- {user.username}")
