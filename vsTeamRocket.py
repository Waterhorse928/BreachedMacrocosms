import math
import random
import charactersPlayer
import charactersEnemy

# Character Lists
playerList = charactersPlayer.tyCharacters
player = {}
enemy = charactersEnemy.rocketCharacters
# Character Slots and Turn Order
turnList = []
slotList = []
slot = {}
# Character Actions to take next
action = {}
target = {}
# extra attacks
# actionEx = {} I'll work on this later
targetEx = {}

# Displays enemies at the start
def encounter ():
    print(f"Encountered {enemy[0]}!")
    print(end="  ")
    for x in range(1, len(enemy)-1):
        print(f"{enemy[x].name},", end=' ')
    print(f"and {enemy[int(len(enemy)-1)].name}!")
 
# displays enemies for selection
def displayEnemies ():
    print(f"{enemy[0]}:")
    for x in range(1, len(enemy)):
        if enemy[x].isAlive == True:
            print(f" {x}. {enemy[x].name}")

# Displays player's characters and asks them to choose a party
def characterSelect ():
    print(f"{playerList[0]}'s Characters:")
    for x in range(1, len(playerList)):
        print(f" {x}. {playerList[x].name}")

    for x in range(1, min(len(playerList), 5)):
        player[x] = input(f"Choose a character for slot {x}: ")
        player[x] = int(player[x])
        player[x] = playerList[player[x]]

# Displays player's slots
def displayPlayers ():
    for x in range(1, len(player)+1):
        print(f" {x}. {player[x].name}")

# Displays skills for a particular character
def listSkills (user):
    print(f"{user.name}'s Skills:")
    for x in range(len(user.skillList)):
        print(f" {x}. {user.skillList[x].name}")

# Use a skill.
def useSkill(user, skill, target):
    user.skillList[skill].skill(user,target)

# use Basic Attack
def useBasicAttack (user, target):
    user.skillList[0].skill(user,target)

# choose actions loop
def chooseActions ():
    for x in range(1, len(player)+1):
        if player[x].isAlive == True:
            listSkills (player[x])
            action[x] = int(input("Choose a skill: "))
            if player[x].skillList[action[x]].type == 1 or player[x].skillList[action[x]].type ==  3:
                displayPlayers ()
                target[x] = player[int(input("Choose a target for skill: "))]
                displayEnemies ()
                targetEx[x] = enemy[int(input("Choose a target for extra attack: "))]
            else:
                displayEnemies ()
                target[x] = enemy[int(input("Choose a target for skill: "))]
                targetEx[x] = 0
        else:
            action[x] = 0
            target[x] = enemy[random.randint(1, len(enemy)-1)]

# chooses enemy actions and targets
def enemyActions ():
    players = len(player)
    for x in range(1, len(enemy)):
        action[x+players] = random.randint(0, len(enemy[x].skillList)-1)
        targetEx[x+players] = 0
        targeted = False
        while not targeted:
            target[x+players] = player[random.randint(1, players)]
            if target[x+players].isAlive == True:
                targeted = True

# Helps turnOrder sort or something
def turnKey(self):
    return self.turnNumber

# redefines turnList, slotList and slot
def turnOrder ():
    turnList.clear ()
    slotList.clear ()
    # add all characters to turnList    
    for x in range(1, len(player)+1):
        turnList.insert(x, player[x])
    for x in range(1, len(enemy)):
        turnList.insert(x+int(len(player)), enemy[x])
    # slot part
    for x in range(1, len(turnList)+1):
        slot[x] = turnList[x-1]
    slotList.extend(turnList)
    # sort turnList
    for x in turnList:
        x.turnNumber = x.spd + random.randint(0, 5)
    turnList.sort(key = turnKey, reverse = True)

# a round of combat
def round ():
    for x in range(0, len(turnList)):
        y = slotList.index(turnList[x])+1
        slot[y].statUpdate ()
        target[y].statUpdate ()
        if slot[y].isAlive == True:
            useSkill(slot[y], action[y], target[y])
            slot[y].statUpdate ()
            target[y].statUpdate ()
            if targetEx[y] != 0:
                useBasicAttack (slot[y], targetEx[y])
            if target[y].hp == 0:
                print(f"{target[y].name} was knocked out!")
    for x in range(1, len(slot)+1):
        slot[x].rotateStatChanges ()

# run the entire battle
def startBattle ():
    encounter ()
    characterSelect ()
    battleOver = False
    playerWon = False
    enemyWon = False
    while battleOver == False:
        chooseActions ()
        turnOrder ()
        enemyActions ()
        round ()
        alivePlayers = 0
        aliveEnemies = 0
        for x in range(1, len(enemy)):
            if enemy[x].isAlive == True:
                aliveEnemies += 1
        for x in range(1, len(player)+1):
            if player[x].isAlive == True:
                alivePlayers += 1        
        if alivePlayers == 0:
            battleOver = True
            enemyWon = True
        if aliveEnemies == 0:
            battleOver = True
            playerWon = True
    if playerWon == True:
        print("You Won!")
    if enemyWon == True:
        print("You Lost...")

startBattle ()
        

