from telethon.tl.functions.contacts import SearchRequest

def run(client):
    print("[*] Searching for public groups/channels...")
    search_query = input("Enter the keyword to search for: ")

    result = client(SearchRequest(q=search_query, limit=10))

    print(f"[*] Found {len(result.chats)} results:")
    for chat in result.chats:
        print(f"- {chat.title} (ID: {chat.id})")
