import random

herolist = ['mage','bard','assassin','warrior','troll','giant']
#create monsterlist
monsterlist = ['bat','goblin','wolf','ogre','elemental','dragon']

#Start of game
lives = 5
roll = random.randint(0,5)
herostrength = roll + 1
hero = herolist[roll] 
print("Welcome " + hero + " : strength " + str(herostrength))

def battle():
    roll = random.randint(0,5)
    monster = monsterlist[roll]
    monsterstrength = (roll + 1)*2
    print("You have encountered a " + monster + ": strength " + str(monsterstrength))
    response = input("Do you wish to fight or flee:")

    if response == "fight":  #selection
        heroroll = random.randint(1,6)
        print("You rolled: " + str(heroroll))
        totalstrength = heroroll + herostrength
        print("You have total strength: " + str(totalstrength))
        monsterroll = random.randint(1,6)
        print("Monster rolled: " + str(heroroll))
        monstertotalstrength = monsterroll + monsterstrength
        print("Monsters total strength: " + str(monstertotalstrength))
    return

battle()
