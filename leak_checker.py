def check_leaks(query):
    """ Check for leaks using Google search (Dorking) """
    print(f"[*] Searching for leaks for {query}")
    results = search_google(query)
    
    if results:
        links = re.findall(r'https?://(?:www\.)?([^\s]+)', results)
        print(f"[*] Found the following potential leaks:\n")
        
        found = False
        for link in links:
            if 'pastebin.com' in link or 'github.com' in link:
                print(f"    [*] Leak detected: {link}")
                found = True
        
        if not found:
            print("[*] No leaks found for this query.")
    else:
        print("[*] Could not retrieve search results. Try again later.")
