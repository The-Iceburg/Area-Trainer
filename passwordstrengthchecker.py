acceptedchar = ["!","$","%","^","&","*","(",")","-","_","=","+","1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P","a","s","d","f","g","h","j","k","l","A","S","D","F","G","H","J","K","L","z","x","c","v","b","n","m","Z","X","C","V","B","N","M"]
acceptedsymb = ["!","$","%","^","&","*","(",")","-","_","=","+"]
unacceptedcombos = ["qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop", "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", "vbn", "bnm"]

def passwordcheck(password): 
    matched_list = [characters in acceptedchar for characters in password]
    string_contains_char = all(matched_list)
    if string_contains_char:
        score = len(password)
        for character in password:
            if character.isupper():
                score += 5
                contupper = True
                break
            else:
                contupper = False
        for character in password:
            if character.islower():
                score += 5
                contlower = True
                break
            else:
                contlower =  False
        for character in password:
            if character.isdigit():
                score += 5
                contnumb = True
                break
            else:
                contnumb = False
        matched_list = [characters in acceptedsymb for characters in password]
        countyranger = len(matched_list)
        for i in range(countyranger):
            if matched_list[i] == True:
                score += 5
                contsymb = True
                break
            else:
                contsymb = False
        if contupper == True and contlower == True and contnumb == True and contsymb == True:
            score += 10
        if password.isalpha():
            score -=5
        if password.isdigit():
            score -=5
        matched_list = [characters in acceptedsymb for characters in password]
        string_contains_symb = all(matched_list)
        if string_contains_symb == True:
            score -=5
        ranger = len(password) - 2
        for i in range(ranger):
            passwordlist = [char for char in password.lower()]
            split = slice(i , i+3)
            string = "".join(passwordlist[split])          
            for j in range(20):
                if string == unacceptedcombos[j]:
                    score -= 5
        if score > 20:
            strenth = "Strong"
        elif score <= 0:
            strenth = "Weak"
        else:
            strenth = "Medium"
    return strenth