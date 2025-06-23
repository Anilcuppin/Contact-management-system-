import json
import os

# The name of the file where contacts will be stored.
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """
    Loads contacts from the JSON file.
    If the file doesn't exist, it returns an empty list.
    """
    # Check if the contacts file exists.
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        # Open and load the contacts from the JSON file.
        with open(CONTACTS_FILE, 'r') as f:
            contacts = json.load(f)
            return contacts
    except (json.JSONDecodeError, IOError):
        # If the file is empty or corrupted, return an empty list.
        return []

def save_contacts(contacts):
    """
    Saves the list of contacts to the JSON file.
    """
    # Open the file in write mode to save the contacts.
    with open(CONTACTS_FILE, 'w') as f:
        # Dump the contacts list into the file with indentation for readability.
        json.dump(contacts, f, indent=4)

def display_contact(contact):
    """Prints the details of a single contact in a formatted way."""
    print("-" * 20)
    print(f"Name:    {contact['name']}")
    print(f"Phone:   {contact['phone']}")
    print(f"Email:   {contact['email']}")
    print(f"Address: {contact['address']}")
    print("-" * 20)

def add_contact(contacts):
    """
    Prompts the user for new contact details and adds it to the list.
    """
    print("\n--- Add a New Contact ---")
    name = input("Enter name: ")
    # Check if a contact with the same name already exists.
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nA contact with this name already exists.")
            return

    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print("\nContact added successfully!")

def view_all_contacts(contacts):
    """
    Displays all saved contacts.
    """
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        display_contact(contact)

def search_contact(contacts):
    """
    Searches for contacts by name.
    """
    print("\n--- Search for a Contact ---")
    search_term = input("Enter the name to search for: ").lower()
    
    # Find all contacts where the name contains the search term.
    found_contacts = [
        contact for contact in contacts 
        if search_term in contact['name'].lower()
    ]

    if not found_contacts:
        print("No contact found with that name.")
        return

    print(f"\nFound {len(found_contacts)} contact(s):")
    for contact in found_contacts:
        display_contact(contact)

def update_contact(contacts):
    """
    Updates an existing contact's information.
    """
    print("\n--- Update a Contact ---")
    name_to_update = input("Enter the name of the contact to update: ").lower()

    contact_to_update = None
    contact_index = -1

    # Find the exact contact to update.
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name_to_update:
            contact_to_update = contact
            contact_index = i
            break

    if not contact_to_update:
        print("Contact not found.")
        return

    print("\nFound contact. Press Enter to keep the current information.")
    
    # Get new details, keeping the old ones if the user just hits Enter.
    new_name = input(f"New name ({contact_to_update['name']}): ") or contact_to_update['name']
    new_phone = input(f"New phone ({contact_to_update['phone']}): ") or contact_to_update['phone']
    new_email = input(f"New email ({contact_to_update['email']}): ") or contact_to_update['email']
    new_address = input(f"New address ({contact_to_update['address']}): ") or contact_to_update['address']
    
    # Update the contact in the list.
    contacts[contact_index] = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "address": new_address,
    }

    save_contacts(contacts)
    print("\nContact updated successfully!")

def delete_contact(contacts):
    """
    Deletes a contact from the list.
    """
    print("\n--- Delete a Contact ---")
    name_to_delete = input("Enter the name of the contact to delete: ").lower()

    contact_to_delete = None
    # Find the contact to delete.
    for contact in contacts:
        if contact['name'].lower() == name_to_delete:
            contact_to_delete = contact
            break
            
    if not contact_to_delete:
        print("Contact not found.")
        return

    # Remove the contact from the list.
    contacts.remove(contact_to_delete)
    save_contacts(contacts)
    print("\nContact deleted successfully!")

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    contacts = load_contacts()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_all_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nExiting the Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
