dictionaryExample = {
    "billnye": [8,7,6],
    "josh": [10,10,10]
}
f = open("scores.txt","a")
f.write(str(dictionaryExample))
f.close()