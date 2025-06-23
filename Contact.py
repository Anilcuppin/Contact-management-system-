import os

CONTACTS_FILE = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = f"{name},{phone},{email}\n"
    with open(CONTACTS_FILE, "a") as file:
        file.write(contact)
    print("Contact added successfully!")

def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found.")
        return

    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("No contacts found.")
            return

        print("\n--- All Contacts ---")
        for index, contact in enumerate(contacts, start=1):
            name, phone, email = contact.strip().split(",")
            print(f"{index}. Name: {name}, Phone: {phone}, Email: {email}")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False

    with open(CONTACTS_FILE, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if search_name in name.lower():
                print(f"Found: Name: {name}, Phone: {phone}, Email: {email}")
                found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ").lower()
    updated = False

    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()

    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            if name.lower() == name_to_update:
                print("Enter new details:")
                name = input("New name: ")
                phone = input("New phone number: ")
                email = input("New email: ")
                updated = True
            file.write(f"{name},{phone},{email}\n")

    if updated:
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").lower()
    deleted = False

    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()

    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            if name.lower() != name_to_delete:
                file.write(f"{name},{phone},{email}\n")
            else:
                deleted = True

    if deleted:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
