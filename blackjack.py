import random
cardpack = [] #keeps a track of card that have dealt

def createcardpack():
    global cardpack
    suits = ["hearts","diamonds","clubs","spades"]
    for suit in suits:
        for i in range(1,14):
            cardpack.append(str(i) + " " + suit)
    return

def deal():
    cardindex = random.randint(0,len(cardpack)-1)
    card = cardpack[cardindex]
    cardpack.remove(card)
    return card

createcardpack()
for c in range(52):
    card = deal()
    print(card)







#players hand is a list

#computer get dealt a card

#show the user their cards

#user is asked to flip to sit

#repeat until sit or bust

#calculate the sum of cards

