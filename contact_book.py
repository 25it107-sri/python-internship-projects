while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Contact
    if choice == 1:

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        with open("contacts.txt", "a") as file:
           file.write(name + "," + phone + "," + email + "\n")

        print("Contact Added Successfully!")

    # View Contacts
    elif choice == 2:

        try:
            with open("contacts.txt", "r") as file:

                contacts = file.readlines()
                print(f"\nTotal Contacts: {len(contacts)}")

                if len(contacts) == 0:
                    print("No Contacts Found!")

                else:
                    print("\n===== CONTACT LIST =====")

                    for contact in contacts:

                        name, phone, email = contact.strip().split(",")

                        
                        print("Name :", name)
                        print("Phone:", phone)
                        print("Email:", email)
                        print("-------------------")

        except FileNotFoundError:
            print("No Contacts Found!")

    # Search Contact
    elif choice == 3:

        search_name = input("Enter name to search: ")

        found = False

        try:
            with open("contacts.txt", "r") as file:

                contacts = file.readlines()

                for contact in contacts:

                    name, phone, email = contact.strip().split(",")

                    if name.lower() == search_name.lower():

                        print("\nContact Found!")
                        print("Name :", name)
                        print("Phone:", phone)
                        print("Email:", email)

                        found = True
                        break

            if not found:
                print("Contact Not Found!")

        except FileNotFoundError:
            print("No Contacts Found!")

    # Update Contact
    elif choice == 4:

        search_name = input("Enter contact name to update: ")

        found = False
        updated_contacts = []

        try:
            with open("contacts.txt", "r") as file:

                contacts = file.readlines()

                for contact in contacts:

                    name, phone, email = contact.strip().split(",")

                    if name.lower() == search_name.lower():

                        print("Current Phone:", phone)

                        new_phone = input("Enter New Phone Number: ")
                        new_email = input("Enter New Email: ")
                        
                        updated_contacts.append(name + "," + new_phone + "," + new_email + "\n" )
    
                        found = True

                    else:
                        updated_contacts.append(contact)

            with open("contacts.txt", "w") as file:
                file.writelines(updated_contacts)

            if found:
                print("Contact Updated Successfully!")
            else:
                print("Contact Not Found!")

        except FileNotFoundError:
            print("No Contacts Found!")

        # Delete Contact
    elif choice == 5:

        search_name = input("Enter contact name to delete: ")

        found = False
        updated_contacts = []

        try:
            with open("contacts.txt", "r") as file:

                contacts = file.readlines()

                for contact in contacts:

                    name, phone = contact.strip().split(",")

                    if name.lower() == search_name.lower():

                        found = True

                    else:
                        updated_contacts.append(contact)

            with open("contacts.txt", "w") as file:
                file.writelines(updated_contacts)

            if found:
                print("Contact Deleted Successfully!")
            else:
                print("Contact Not Found!")

        except FileNotFoundError:
            print("No Contacts Found!")
    # Exit
    elif choice == 6:

        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid Choice!")