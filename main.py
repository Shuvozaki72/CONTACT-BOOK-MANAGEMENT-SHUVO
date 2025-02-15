from contact_manage import ContactManager
def main():
    
    contact = ContactManager()
    
    while True:
        print("\n----Contact Book Management System----")
        print("1. Add contact")
        print("2. View contact")
        print("3. Remove contact")
        print("4. Search contact")
        print("5. Exit")
        
        choise = input("Select a option (1-5): ")
        
        if choise == '1':
            contact.add_contact()
            
        if choise == '2':
            contact.contact_view()
            
        if choise == '3':
            contact.delete_contact()
        
        if choise == '4':
            contact.search_contact()
            
        if choise == '5':
            print("Thank you for use contact management system")
            break
    
if __name__ == "__main__":
    main()