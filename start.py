def main_menu():
    print("Welcome to Personal Jarvis!")
    print("Please select an option:")
    print("1. Start Personal Jarvis")
    print("2. Help")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == '1':
        print("Starting Personal Jarvis...")
        # Add logic to start Personal Jarvis
    elif choice == '2':
        print("Help instructions will be here.")
        # Add help instructions
    elif choice == '3':
        print("Exiting. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()