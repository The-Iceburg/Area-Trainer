from passwordstrengthchecker import passwordcheck as pc

tilda = ["~"]

def menu():

    choice = int(input("##############################################\nPlease select your option from the list below:\n1. Login\n2. Register\n3. Quit\n##############################################\n"))

    if choice == 1:
        username = str(input("##############################################\nPlease enter your username:\n##############################################\n"))
        file = open('logins.txt','r')
        logins = file.readlines()
        for i in range(len(logins)):
            string = logins[i].split("~")
            string[1] = string[1].strip("\n")
            if string[0] == username:
                password = str(input("##############################################\nPlease enter your password:\n##############################################\n"))
                if string[1] == password:
                    shapemen()
                    break
                else:
                    print("##############################################\nPassword Incorrect")
                    menu()
        file.close()

    
    elif choice == 2:
        username = str(input("##############################################\nPlease enter a username:\n##############################################\n"))
        matched_list = [characters in tilda for characters in username]
        string_contains_tilda = all(matched_list)
        if string_contains_tilda == True:
            print("##############################################\nTildas '~' aren't accepted in usernames please re-register")
            menu()
        else:
            file = open('logins.txt','r')
            logins = file.readlines()
            for i in range(len(logins)):
                string = logins[i].split("~")
                if string[0] == username:
                    print("##############################################\nThis username already exists! Please enter another")
                    menu()
            file.close()

            password = str(input("##############################################\nPlease enter a password:\n##############################################\n"))
            matched_list = [characters in tilda for characters in username]
            string_contains_tilda = all(matched_list)
            if string_contains_tilda == True:
                print("##############################################\nTildas '~' aren't accepted in passwords please re-register")
                menu()
            else:

                strength = pc(password)

                if strength == "Strong" or strength == "Medium":
                    f = open("logins.txt", "a")
                    f.write("\n")
                    f.write(username)
                    f.write("~")
                    f.write(password)
                    f.close()
                else:
                    print("##############################################\nYour password doesn't meet our requirements please re-register")
                    menu()
            
    elif choice == 3:
        print("##############################################\nThanks for using the area trainer!\n##############################################\n")
        exit()
    else:
        print("##############################################\nUnable to load page\nPlease enter a valid integer 1 - 3")
        menu()

def shapemen():
    choice = int(input("##############################################\nPlease select your option from the list below:\n1. Triangle\n2. Rectangle\n3. Circle\n4. Quit (Logout)\n##############################################\n"))
    if choice == 1:
        print("Triangle")
    elif choice == 2:
        print("Rectangle")
    elif choice == 3:
        print("Circle")
    elif choice == 4:
        print("##############################################\nSuccesfully logged out!\nThanks for using the area trainer!\n##############################################\n")
        exit()
    else:
        print("##############################################\nUnable to load page\nPlease enter a valid integer 1 - 3")
        shapemen()
menu()