
import random
import string

passwords = {}

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    print ("===== PASSWORD MANAGER =====")
    print ("1. Add Password")
    print ("2. View Password")
    print ("3. Search Password")
    print ("4. Delete Password")
    print ("5. Generate Password")
    print ("6. Exit")

    user = int(input("Enter your choice: "))

    if user == 1:
        website = input("Enter website: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        passwords[website] = {
            "username": username,
            "password": password,
        }

        print ("Password added successfully!")

    elif user == 2:
        if len(passwords) == 0:
            print ("No password saved")

        else:
            for website, details in passwords.items():
                        print (f"Website: {website}")
                        print (f"Username: {details['username']}")   
                        print (f"Password: {details['password']}")

    elif user == 3:
        website = input("Enter website to search: ")
        if website in passwords:
             print ("Website found!")
             print (f"Website: {website}")
             print (f"Username: {passwords[website]['username']}")
             print (f"Password: {passwords[website]['password']}")

        else:
             print ("website not found")

    elif user == 4:
        print ("Delete password")
        delete = input("enter website to delete: ")
        if delete in passwords:
             passwords.pop(delete)
             print("Password deleted successfully!")
        else:
             print("website not valid")

    elif user == 5:
         print("===== PASSWORD GENERATOR =====")
         length = int(input("Enter password length: "))
         generate_password = ""

         for i in range (length):
              generate_password += random.choice(characters)

         print (f"Generated password: {generate_password}")
         
    

    elif user == 6:
        break

    else:
        print ("please enter valid input")