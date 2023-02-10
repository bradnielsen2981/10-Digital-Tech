import random
#Start of game
herolist = ['mage','bard','assassin','warrior','troll','giant']
monsterlist = ['bat','goblin','wolf','ogre','elemental','dragon'] #create monsterlist
lives = 5
roll = random.randint(0,5)
herostrength = roll + 1
hero = herolist[roll] 
score = 0

print("Welcome " + hero + " : strength " + str(herostrength))
def battle():
    global score
    global lives
    global herostrength
    roll = random.randint(0,5)
    monster = monsterlist[roll]
    monsterstrength = (roll + 1)*2
    print("You have encountered a " + monster + ": strength " + str(monsterstrength))
    response = input("Do you wish to fight or flee:")

    if response == "fight":  #CONDITION = TRUE OR FALSE
        heroroll = random.randint(1,6)
        print("You rolled: " + str(heroroll))
        totalstrength = heroroll + herostrength
        print("You have total strength: " + str(totalstrength))
        monsterroll = random.randint(1,6)
        print("Monster rolled: " + str(heroroll))
        monstertotalstrength = monsterroll + monsterstrength
        print("Monsters total strength: " + str(monstertotalstrength))

        if totalstrength > monstertotalstrength:
            print("You have vanquished the " + monster)
            score = score + roll
            print("YOUR SCORE IS: " + str(score))
            if score%7 == 0:
                herostrength = herostrength + 1 
        elif totalstrength == monstertotalstrength:
            print("Stalemate. The Monster flees.")
        else:
            print("You have died horribly!!!! You lose a life")
            lives = lives - 1

    elif response == "flee":
        heroroll = random.randint(1,6)
        print("You rolled: " + str(heroroll))
        if hero >= 4:
            print("You escaped!!")
        else:
            print("You have died horribly!!!! You lose a life")
    print("==========================================")
    return


while True:
    battle()
