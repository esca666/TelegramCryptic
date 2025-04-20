from group_finder import find_telegram_groups

def main():
    print("\n[*] Welcome to Cryptic OSINT Tool")
    print("[*] Choose a module (1-5):\n")
    print("1. Find Groups/Channels")
    print("2. Extract Members")
    print("3. Analyze Messages")
    print("4. Check for Leaks")
    print("5. Real-Time Monitoring")

    choice = input("Enter choice: ")

    if choice == "1":
        find_telegram_groups()
    elif choice == "2":
        # Your extract members function
        pass
    elif choice == "3":
        # Your analyze messages function
        pass
    elif choice == "4":
        # Your leak checker function
        pass
    elif choice == "5":
        # Your real-time monitoring function
        pass
    else:
        print("[*] Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
