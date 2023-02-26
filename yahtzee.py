import random

reddice = random.randint(1,6)
greendice = random.randint(1,6)
attempts = 5

while (reddice != greendice) and (attempts > 0): #loop WHILE condition = true
    attempts = attempts - 1
    print("Red: " + str(reddice) + " Green: " + str(greendice) + " Attempts remaining: " + str(attempts))
    reddice = random.randint(1,6)
    greendice = random.randint(1,6)

if attempts == 0:
    print("You died! Game over man!")
else:
    print('Yahtzee')
