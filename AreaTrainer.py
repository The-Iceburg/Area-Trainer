from passwordstrengthchecker import passwordcheck as pc
import os

tilda = ["~"]
filedir = os.getcwd() + "\logins.txt"

def menu():

    choice = int(input("##############################################\nPlease select your option from the list below:\n1. Login\n2. Register\n3. Quit\n##############################################\n"))

    if choice == 1:
        print("choice 1")
    elif choice == 2:
        username = str(input("##############################################\nPlease enter a user name:\n##############################################\n"))
        matched_list = [characters in tilda for characters in username]
        string_contains_tilda = all(matched_list)
        if string_contains_tilda == True:
            print("##############################################\nTildas '~' aren't accepted in usernames please re-register")
            menu()
        else:
            password = str(input("##############################################\nPlease enter a password:\n##############################################\n"))
            matched_list = [characters in tilda for characters in username]
            string_contains_tilda = all(matched_list)
            if string_contains_tilda == True:
                print("##############################################\nTildas '~' aren't accepted in passwords please re-register")
                menu()
            else:

                strength = pc(password)

                print(strength)

                if strength == "Strong" or strength == "Medium":
                    f = open(filedir, "a")
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
    
menu()
