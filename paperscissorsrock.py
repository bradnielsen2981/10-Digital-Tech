# DECOMPOSITION
import random
movelist = ['paper','scissors','rock']
playermove = ""

#compare move will return true if p is better than c
def comparemove(p,c):
    print("Player: " + p + " Computer: " + c)
    if p == c:
        print("Draw")
    else: 
        if (p == "paper" and c == 'rock') or (p == "scissors" and c == 'paper') or (p == "rock" and c == 'scissors'):
            print("Win")
            return True
        else:
            print("Lose!")
            return False
    return False

#Continually play the game until player wants to quit
while playermove != 'exit':
    # Computer will choose a random move from paper scissors rock
    computermove = random.choice(movelist)
    # Player will choose a move from paper scissors rock
    playermove = input("paper, scissor, rock, or exit? ")
    if playermove != 'exit':
        if playermove in movelist:
            # Comparison of Computers move to players move to decide who wins
            result = comparemove(playermove,computermove)
print("Goodbye")