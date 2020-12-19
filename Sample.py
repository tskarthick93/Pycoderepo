#print("Py")
#print("Python")
# Prompt the user to enter a word
# and assign it to the userWord variable.
#userWord=input("Enter a string :")
#userWord=userWord.upper()

#print("Py",userWord)
#userWord=userWord.upper(input("Enter a string :"))
#for letter in userWord:
#    if letter in userWord
#    if letter in userWord != 'a':
        #userWord=userWord.replace('a')
#        print(letter)
    # Complete the body of the for loop.
wordWithoutVowels = ""

user = input("Enter a word: ")
userWord  = user.upper()


for letter in userWord:
    if letter == "A":
        print(letter,userWord)
        continue
    elif letter == "E":
        continue
    elif letter == "O":
        continue
    elif letter == "I":
        continue
    elif letter == "U":
        continue
        print(letter,userWord)
    else:
        wordWithoutVowels += letter

print(wordWithoutVowels)
