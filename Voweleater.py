wordWithoutVovels = ""
userWord = input().upper()
for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        wordWithoutVovels += letter
print (wordWithoutVovels)



