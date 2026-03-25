"""
Contact Book (Console Application)
---------------------------------
Meets requirements:
1. Add contact (persisted to contacts.json)
2. View list of contacts
3. Delete contact by name
4. Search contacts by name
5. Menu-driven interface
6. Input validation (name = letters/spaces only, phone = digits only)
7. Uses JSON file: contacts.json
8. Well-commented for beginners
"""

import json
import os

FILE_NAME = "contacts.json"

# -----------------------------
# File Handling Functions
# -----------------------------

def load_contacts():
    """Load contacts from JSON file. If file doesn't exist, return empty list."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If file is corrupted or empty
        return []


def save_contacts(contacts):
    """Save contacts list to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# -----------------------------
# Validation Functions
# -----------------------------

def valid_name(name):
    """Check that name contains only letters and spaces."""
    return all(char.isalpha() or char.isspace() for char in name) and name != ""


def valid_phone(phone):
    """Check that phone contains only digits."""
    return phone.isdigit() and phone != ""

# -----------------------------
# CRUD Functions
# -----------------------------

def add_contact():
    """Add a new contact with validation."""
    name = input("Enter name: ")
    if not valid_name(name):
        print("Invalid name. Use letters only.")
        return

    phone = input("Enter phone: ")
    if not valid_phone(phone):
        print("Invalid phone. Use digits only.")
        return

    address = input("Enter address: ")
    email = input("Enter email: ")

    contacts = load_contacts()

    # Prevent duplicate names
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact with this name already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "address": address,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!\n")


def view_contacts():
    """Display all contacts."""
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Address: {contact['address']}")
        print(f"Email: {contact['email']}")
        print("--------------------")


def delete_contact():
    """Delete a contact by name."""
    name = input("Enter name to delete: ")
    contacts = load_contacts()

    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]

    if len(new_contacts) == len(contacts):
        print("Contact not found.\n")
        return

    save_contacts(new_contacts)
    print("Contact deleted successfully!\n")


def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").lower()
    contacts = load_contacts()

    found = False
    for contact in contacts:
        if name in contact["name"].lower():
            print("\n--- Match Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Address: {contact['address']}")
            print(f"Email: {contact['email']}")
            print("-------------------")
            found = True

    if not found:
        print("No matching contact found.\n")

# -----------------------------
# Menu System
# -----------------------------

def menu():
    """Display menu options."""
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")


def main():
    """Main program loop."""
    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# Run the program
if __name__ == "__main__":
    main()
