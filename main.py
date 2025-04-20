import pyfiglet
from config import get_client
import group_scraper
import member_extractor
import message_analyzer
import leak_checker
import monitor

def display_banner():
    banner = pyfiglet.figlet_format("Cryptic", font="slant")  # Hacker-themed font
    print(banner)
    print("[*] Welcome to Cryptic OSINT Tool")
    print("[*] Created by Cryptic")
    print("[*] For educational purposes only. Use responsibly.")
    print("[*] Code by: Cryptic")
    print("[*] Let's dive into the world of OSINT...")

# Call display_banner() before the main menu
display_banner()

print("Telegram OSINT Tool")
print("1. Find Groups/Channels")
print("2. Extract Members")
print("3. Analyze Messages")
print("4. Check for Leaks")
print("5. Real-Time Monitoring")

choice = input("Choose a module (1-5): ")
client = get_client()

if choice == "1":
    group_scraper.run(client)
elif choice == "2":
    member_extractor.run(client)
elif choice == "3":
    message_analyzer.run(client)
elif choice == "4":
    leak_checker.run()
elif choice == "5":
    monitor.run(client)
else:
    print("Invalid choice.")
