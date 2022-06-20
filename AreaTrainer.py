import random
import math

from passwordstrengthchecker import passwordcheck as pc

possanswers = [1,2,3,4]

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
        matched_list = [characters in ["~"] for characters in username]
        string_contains_tilda = any(matched_list)
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
            matched_list = [characters in ["~"] for characters in password]
            string_contains_tilda = any(matched_list)
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
    choice = int(input("##############################################\nPlease select your option from the list below:\n1. Triangle △\n2. Rectangle ▯\n3. Circle ○\n4. Quit (Logout)\n##############################################\n"))
    if choice == 1:

        perpheight = random.randint(2,15)
        width = random.randint(2,15)

        answer = perpheight * width / 2

        for i in range(4):
            
            perpheightpred = random.randint(2,15)
            widthpred = random.randint(2,15)

            answerpred = perpheightpred * widthpred / 2

            possanswers[i] = answerpred

        answerno = random.randint(0,3)
        possanswers[answerno] = answer

        question = int(input("##############################################\n△ - Triangle\n\nPerpendicular Height = " + str(perpheight) +"\nWidth = " + str(width) + "\n\n1. " + str(possanswers[0])+ " 2. " + str(possanswers[1]) + " 3. " + str(possanswers[2]) + " 4. " + str(possanswers[3]) + "\n##############################################\n"))
        if question == answerno + 1:
            print("correct")
        else:
            print("incorrect")

    elif choice == 2:
        
        height = random.randint(2,15)
        width = random.randint(2,15)

        answer = height * width

        for i in range(4):
            
            heightpred = random.randint(2,15)
            widthpred = random.randint(2,15)

            answerpred = heightpred * widthpred
            possanswers[i] = answerpred

        answerno = random.randint(0,3)
        possanswers[answerno] = answer

        question = int(input("##############################################\n▯ - Rectangle\n\nWidth = " + str(width) +"\nHeight = " + str(height) +"\n\n1. " + str(possanswers[0])+ " 2. " + str(possanswers[1]) + " 3. " + str(possanswers[2]) + " 4. " + str(possanswers[3]) + "\n##############################################\n"))
        if question == answerno + 1:
            print("correct")
        else:
            print("incorrect")

    elif choice == 3:
        
        radius = random.randint(2,15)

        answer = math.pi * (radius**2)
        answer = round(answer, 2)

        for i in range(4):
            
            radiuspred = random.randint(2,15)

            answerpred = math.pi * (radiuspred**2)
            answerpred = round(answerpred, 2)
            possanswers[i] = answerpred

        answerno = random.randint(0,3)
        possanswers[answerno] = answer

        question = int(input("##############################################\n○ - Circle\n\nRadius = " + str(radius) +"\n\n1. " + str(possanswers[0])+ " 2. " + str(possanswers[1]) + " 3. " + str(possanswers[2]) + " 4. " + str(possanswers[3]) + "\n\nGive your answer rounded to 2.dp\n##############################################\n"))
        if question == answerno + 1:
            print("correct")
        else:
            print("incorrect")

    elif choice == 4:
        print("##############################################\nSuccesfully logged out!\nThanks for using the area trainer!\n##############################################\n")
        exit()
    else:
        print("##############################################\nUnable to load page\nPlease enter a valid integer 1 - 3")
        shapemen()
menu()