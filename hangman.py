word = input("Please enter the word: ")
wordblank = "_"*len(word)
wordblank = list(wordblank) #list
lives = 7

while lives > 0:
    letter = input("Type a letter: ")
    letterfound = False
    for index in range(len(word)):
        print(word[index])
        if word[index] == letter:
            wordblank[index] = letter
            letterfound = True
    if letterfound == False:
        lives = lives - 1
        print("You lost a life! " + str(lives) + " remaining." )
    print(wordblank)
    if wordblank == list(word):
        print("You have survived punk! I will hang you next time")
        break



