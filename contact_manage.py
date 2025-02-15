from validation import check_valid_name, check_number, check_email
import json
class ContactManager():
    
    
    contacts = []
    def __init__(self, *args, **kwargs):
        with open('Contacts.txt', 'r') as file:
            for line in file:
                fields = line.strip().split(", ")
                contact = {}
                for field in fields:
                    key, value = field.split(": ", 1)  # Split by ': ' to separate key and value
                    contact[key.lower()] = value  # Use lowercase keys for consistency
                self.contacts.append(contact)
    
    
    def add_contact(self):
        name = input("Please Enter name: ").strip()
        email = input("Please Enter email: ").strip()
        phone = input("Please Enter phone number: ").strip()
        address = input("Please Enter address: ").strip()
        
        # check validation of email
        if not check_email(email):
            print("Please Enter a valid email.")
            return
        # check validation of phone number
        elif not check_number(phone):
            print("Phone number can't contain string.")
            return
        # check validation of name
        elif not check_valid_name(name):
            print("Name only can contain string.")
            return
        
        # check have duplicat number or not
        for i in self.contacts:
            if (i['phone']) == phone:
                print("Phone number already exist. Please try with another number!")
                return
            
        

        new_contact = {'name':name, 'email':email, 'phone':phone, 'address':address}
        self.contacts.append(new_contact)
        with open('Contacts.txt', 'w') as file:  # Use 'w' mode for writing
            for contact in self.contacts:
                # Convert each contact (a dictionary) to a string
                contact_str = f"name: {contact['name']}, email: {contact['email']}, phone: {contact['phone']}, address: {contact['address']}\n"
                file.write(contact_str)
                
        print("New Contact successfully added to the contact book!")
        
    
    def contact_view(self):
        if not self.contacts:
            print("No contact available in your contact list")
            return
        print("\n--- Contact List ---")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
            
            
    def search_contact(self):
        query = input("Please Enter name for search contact: ").strip()
        for contact in self.contacts:
            if query.lower() == (contact['name']).lower():
                print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
                
                
            

    def delete_contact(self):
        query = input("Enter name for delete contact..: ").strip()
        for index, contact in enumerate(self.contacts):
            if query.lower() in str(contact).lower():
                self.contacts.pop(index)
                with open('Contacts.txt', 'w') as file:  # Use 'w' mode for writing
                    for contact in self.contacts:
                        # Convert each contact (a dictionary) to a string
                        contact_str = f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}\n"
                        file.write(contact_str)
                print("Contact Successfully removed!")
                return index
            print("No contact found!")
            