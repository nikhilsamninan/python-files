def print_menu():
    print('1. Print all contacts')
    print('2. Add a Contact')
    print('3. Search  Phone Number')
    print('4. Edit a Phone Number')
    print('5. Remove a contact')
    print('6. Quit')

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 6:
    menu_choice = int(input("Type a number (1-6): "))
    if menu_choice == 1:
        k= open("phone_Book.txt",'r+')
        s = k.read()
        print(s)
        k.close()
    elif menu_choice == 2:
        k= open("phone_Book.txt",'r+')
        if k.readlines():
        # this code work only if any value in the txt file 
            k=open("phone_Book.txt",'r+')
            s = k.read()
            numbers = eval(s)
            k.close()
            s = open("phone_book.txt",'w+')
            print("Enter the name and number to add")
            access = "true"
            while(access == "true"):
                print("Add Name and Number")
                name = input("Name: ")
                phone = input("Number: ")
                numbers[name] = phone
                print("Contact added successfully")
                break
            s.write(str(numbers))
            s.close()
        else:
        # this code is to add contact as txt file is empty 
            s=open("phone_Book.txt",'w+')
            print("Enter the name and number to add")
            access = "true"
            numbers = {}
            while(access == "true"):
                print("Add Name and Number")
                name = input("Name: ")
                phone = input("Number: ")
                numbers[name] = phone
                print("Contact added successfully")
                break
            s.write(str(numbers))
            s.close()
    elif menu_choice == 3:              #this code is to search contact
        k=open("phone_Book.txt",'r+')
        s = k.read()
        numbers = eval(s)
        k.close()
        name = input("Enter the Name to search: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice == 4:     #this code is to edit the contact(name or number) 
        k=open("phone_Book.txt",'r+')
        s = k.read()
        numbers = eval(s)
        k.close()
        n=int(input("Do you want to edit name or number 1.name and 2.number"))
        if(n == 1):
            s = open("phone_book.txt",'w+')
            access = "true"
            while(access == "true"):
                old_key = input("Enter the name you want to change:")
                new_key = input("Enter the new name")
                numbers[new_key] = numbers.pop(old_key)
                break
            s.write(str(numbers))
            s.close()
        elif(n == 2):
            s = open("phone_book.txt",'w+')
            access = "true"
            while(access == "true"):
                name = input("Enter the name to change number")
                no = input("pls enter the number")
                numbers[name] = no
                break
            s.write(str(numbers))
            s.close()
    elif menu_choice == 5:    #this code is to remove contact from contact list
        k=open("phone_Book.txt",'r+')
        s = k.read()
        numbers = eval(s)
        k.close()
        s = open("phone_book.txt",'w+')
        access = "true"
        while(access == "true"):
            print("Remove Name and Number")
            name = input("Name: ")
            if name in numbers:
                del numbers[name]
                print("Contact Removed Successfully")
            else:
                print(name, "was not found")
            break
        s.write(str(numbers))
        s.close()
    elif menu_choice == 6:  #quit from the program phonebook.py
        print("Thank you for using phone book")
        break











