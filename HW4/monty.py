# CS-171-A Prof Mark Boady
# Homework 4
# Cameron Kelliher
# 11/26/17

import random

random.seed()

def setupDoors():
    doors = ['G', 'G', 'C']
    random.shuffle(doors)
    return doors

def playerDoor():
    return random.randint(1, 3)

def montyDoor(Doors, Player):
     possibleDoors = [1, 2, 3]
     possibleDoors.remove(Player)
     for i in possibleDoors:
         if Doors[i - 1] == 'C':
             possibleDoors.remove(i)
     return random.choice(possibleDoors)

def playRound():
    doors = setupDoors()
    playersDoor = playerDoor()
    montysDoor = montyDoor(doors, playersDoor)

    remainingDoor = [1, 2, 3]
    remainingDoor.remove(playersDoor)
    remainingDoor.remove(montysDoor)
    remainingDoor = remainingDoor[0]

    if doors[remainingDoor - 1] == 'C':
        return 1
    else:
        return 0

def doTests(trials):
    total = 0
    for i in range(0, trials):
        total += playRound()
    switch = total / trials
    stay = 1 - switch
    return stay, switch


print('Welcome to Monty Hall Analysis')
print('Enter \'exit\' to quit.')

while True:
    try:
        userInput = input('How many tests should we run?\n')
        if userInput == 'exit':
            break
        numTests = int(userInput)
        if numTests <= 0:
            print('Bad Input, Please enter a positive number')
            continue

        stay, switch = doTests(numTests)
        print('Stay won %.2f%% of the time' % (stay * 100))
        print('Switch won %.2f%% of the time' % (switch * 100))
    except:
        print('Bad Input, Please enter a number')

