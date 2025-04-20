import requests
import re

def search_google(query):
    """ Perform a Google search and return the first page's HTML results. """
    search_url = f"https://www.google.com/search?q={query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        response.raise_for_status()  # Check for request errors
        return response.text
    except requests.RequestException as e:
        print(f"[!] Error during Google search: {e}")
        return None

def check_leaks(query):
    """ Check for leaks using Google search (Dorking) """
    print(f"[*] Searching for leaks for {query}")
    results = search_google(query)
    
    if results:
        links = re.findall(r'https?://(?:www\.)?([^\s]+)', results)
        print(f"[*] Found the following potential leaks:
")
        
        found = False
        for link in links:
            if 'pastebin.com' in link or 'github.com' in link:
                print(f"    [*] Leak detected: {link}")
                found = True
        
        if not found:
            print("[*] No leaks found for this query.")
    else:
        print("[*] Could not retrieve search results. Try again later.")

def run():
    """ Run the leak checking process """
    print("[*] Checking for leaked data")
    leak_query = input("Enter the data to search for leaks: ")
    check_leaks(leak_query)
