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

def total(hand):
    t = 0
    for card in hand:
        parts = card.split()
        t = t + int(parts[0])
    return t

createcardpack()
playershand = []
computershand = []
playershand.append(deal()) #players hand is a list
playershand.append(deal())
computershand.append(deal()) #computer get dealt a card
print("Player has been dealt " + str(playershand))
print("Computer has been dealt " + str(computershand))
move = input("hit or sit")
while move == "hit":
    playershand.append(deal())
    print("Player has been dealt " + str(playershand))
    print(total(playershand))
    move = input("hit or sit")





