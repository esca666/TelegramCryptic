from telethon.tl.functions.messages import GetParticipantsRequest

def run(client):
    print("[*] Extracting members from a group/channel")
    group_id = input("Enter the group/channel ID: ")

    group = client.get_entity(group_id)
    participants = client(GetParticipantsRequest(group, limit=100))

    print(f"[*] Found {len(participants.users)} members:")
    for user in participants.users:
        print(f"- {user.username}")
