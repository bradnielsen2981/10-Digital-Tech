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
        number = int(parts[0]) 
        if number > 10:
            number = 10
        t = t + number
    print(t)
    return t

def readhand(hand):
    cardtext = ""
    for card in hand:
        components = card.split()
        symbol = components[0]
        if symbol == 1:
            symbol = "Ace"
        elif symbol == 11:
            symbol = "Jack"
        elif symbol == 12:
            symbol == "Queen"
        elif symbol == 13:
            symbol == "King"
        cardtext = str(symbol) + components[1] + " , "
    return cardtext
        
createcardpack()
playershand = []
computershand = []
playershand.append(deal()) #players hand is a list
playershand.append(deal())
computershand.append(deal()) #computer get dealt a card
print("Player has been dealt " + readhand(playershand))
print("Computer has been dealt " + readhand(computershand))

bust = False
while not bust:

    move = input("hit or sit: ")
    if move == "hit":
        playershand.append(deal())
        print("Player's hand is: " + readhand(playershand))
    elif move == "sit":
        break
    
    if total(playershand) > 21:
        bust = True
        print("You busted! Computer wins")

if not bust:
    while total(computershand) < total(playershand):
        computershand.append(deal())
        print("Computers hand is " + readhand(computershand))

if total(computershand) <= 21:
    print("Computer wins!!")
else:
    print("Player wins!!")



