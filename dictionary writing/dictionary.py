dictionaryExample = {}

f = open("scores.txt","r").read()
dictionaryExample = eval(f)

print(dictionaryExample)

f = open("scores.txt", "w")
username = input("username?\n")
score = int(input("score\n"))
value = dictionaryExample.get(username)
value.append(score)
dictionaryExample.update({username: value})

f.write(str(dictionaryExample))
f.close()
print("done")
