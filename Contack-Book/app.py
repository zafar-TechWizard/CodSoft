import json
import os
import time
import msvcrt  # For keyboard input
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

CONTACTS_FILE = "./Contack Book/contacts.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    clear_screen()
    print(Fore.CYAN + "Add New Contact")
    print(Fore.CYAN + "==============")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)

    print(Fore.GREEN + "Contact added successfully!")

def view_contacts(contacts):
    while True: 
        clear_screen()
        print(Fore.CYAN + "Contact List")
        print(Fore.CYAN + "============")

        if contacts:
            for name, info in contacts.items():
                print(Fore.YELLOW + f"Name: {name}")
                print(Fore.YELLOW + f"Phone: {info['phone']}")
                print(Fore.YELLOW + f"Email: {info['email']}")
                print(Fore.YELLOW + f"Address: {info['address']}")
                print("--------------------------------")
                print()
        else:
            print(Fore.RED + "No contacts found.")

        print(Fore.MAGENTA + "Press 'esc' to go back to main menu...")
        
        # Wait for keyboard input
        key = msvcrt.getch()
        if key == b'\x1b':  # Check if 'esc' key is pressed
            break

def search_contact(contacts):
    while True:
        clear_screen()
        print(Fore.CYAN + "Search Contact")
        print(Fore.CYAN + "==============")

        search_term = input("Enter name or phone number to search: ")

        found = False
        for name, info in contacts.items():
            if search_term in [name, info['phone']]:
                print(Fore.YELLOW + f"Name: {name}")
                print(Fore.YELLOW + f"Phone: {info['phone']}")
                print(Fore.YELLOW + f"Email: {info['email']}")
                print(Fore.YELLOW + f"Address: {info['address']}")
                print()
                found = True

        if not found:
            print(Fore.RED + "Contact not found.")

        print(Fore.MAGENTA + "Press 'esc' to go back to main menu...")

        # Wait for keyboard input
        key = msvcrt.getch()
        if key == b'\x1b':  # Check if 'esc' key is pressed
            break

def update_contact(contacts):
    clear_screen()
    print(Fore.CYAN + "Update Contact")
    print(Fore.CYAN + "==============")

    name = input("Enter name of contact to update: ")

    if name in contacts:
        print(Fore.YELLOW + f"Name: {name}")
        print(Fore.YELLOW + f"Phone: {contacts[name]['phone']}")
        print(Fore.YELLOW + f"Email: {contacts[name]['email']}")
        print(Fore.YELLOW + f"Address: {contacts[name]['address']}")
        print()

        choice = input("What would you like to update (phone/email/address)? ").lower()
        if choice == 'phone':
            contacts[name]['phone'] = input("Enter new phone number: ")
        elif choice == 'email':
            contacts[name]['email'] = input("Enter new email address: ")
        elif choice == 'address':
            contacts[name]['address'] = input("Enter new address: ")
        else:
            print(Fore.RED + "Invalid choice!")

        save_contacts(contacts)
        print(Fore.GREEN + "Contact updated successfully!")
    else:
        print(Fore.RED + "Contact not found.")

def delete_contact(contacts):
    clear_screen()
    print(Fore.CYAN + "Delete Contact")
    print(Fore.CYAN + "==============")

    name = input("Enter name of contact to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(Fore.GREEN + "Contact deleted successfully!")
    else:
        print(Fore.RED + "Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        clear_screen()
        print("             " + Fore.CYAN + "Contact Book")
        print("        " + Fore.CYAN + "=====================")
        print("\n    " + Fore.MAGENTA + "1. Add Contact")
        print("    " + Fore.MAGENTA + "2. View Contact List")
        print("    " + Fore.MAGENTA + "3. Search Contact")
        print("    " + Fore.MAGENTA + "4. Update Contact")
        print("    " + Fore.MAGENTA + "5. Delete Contact")
        print("    " + Fore.MAGENTA + "6. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print(Fore.YELLOW + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice!")


        time.sleep(1)

if __name__ == "__main__":
    main()

