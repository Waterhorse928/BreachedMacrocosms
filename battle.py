import math
import random
import charactersPlayer
import charactersEnemy
import time

code = "XXXX"
# Character Lists
playerList = []
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
targetEx = {}

# Displays enemies at the start and removes enemy[0]
def encounter ():
    print(f"Encountered",end=" ")
    for x in range(1, len(enemy)-1):
        print(f"{enemy[x].name},", end=' ')
    print(f"and {enemy[int(len(enemy)-1)].name}!")
    del enemy[0]
 
# displays enemies for selection. Only alive ones
def displayEnemies ():
    for x in range(1, len(enemy)+1):
        if enemy[x].isAlive == True:
            print(f" {x}. {enemy[x].name}")

# Returns a list of alive characters, player or enemy
def listAliveCharacters (dict):
    aliveList = []
    for x in range(1, len(dict)+1):
        if dict[x].isAlive == True:
            aliveList.append(dict[x])
    return aliveList

# Returns a list of useable skills
def listActiveSkills (user):
    activeSkills = []
    for x in range(0, len(user.skillList)):
        if user.skillList[x].cooldown == 0:
            activeSkills.append(x)
    return activeSkills

# lowers skill cooldowns by 1
def lowerSkillCooldown (user):
    for x in user.skillList:
        if x.cooldown != 0:
            x.cooldown -= 1

# Displays player's characters and asks them to choose a party
def characterSelect ():
#    print(f"Characters:")
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
    print(f"--{user.name}-- [{user.hp}/{user.maxHp}] HP")
    for x in range(len(user.skillList)):
        if user.skillList[x].cooldown == 0:
            print(f" {x}. {user.skillList[x].name}")
        else:
            if user.skillList[x].cooldown == 1:
                turns = "turn"
            else:
                turns = "turns"
            print(f" X. {user.skillList[x].name} [Cooldown: {user.skillList[x].cooldown} {turns}]")

# Use a skill.
def useSkill(user, skill, target):
    if target in player.values():
        party = player
    if target in enemy.values():
        party = enemy
    party = listAliveCharacters(party)
    if user.skillList[skill].type in [0,1,2]:
        if target.hp == 0:
            if target in player.values():
                try:
                    target = random.choice(listAliveCharacters(player))
                except:
                    pass
            if target in enemy.values():
                try: 
                    target = random.choice(listAliveCharacters(enemy))
                except:
                    pass
    if target != []:
        user.skillList[skill].skill(user,target,party)

# use Basic Attack
def useBasicAttack (user, target):
    if target in player.values():
        party = player
    if target in enemy.values():
        party = enemy
    party = listAliveCharacters(party)
    if target.hp == 0:
            if target in player.values():
                try:
                    target = random.choice(listAliveCharacters(player))
                except:
                    pass
            if target in enemy.values():
                try: 
                    target = random.choice(listAliveCharacters(enemy))
                except:
                    pass
    user.skillList[0].skill(user,target,party)

# choose actions loop
def chooseActions ():
    for x in range(1, len(player)+1):
        if player[x].isAlive == True:
            listSkills (player[x])
            action[x] = int(input("Choose a skill: "))
            if player[x].skillList[action[x]].type in [1,2,3]:
                if player[x].skillList[action[x]].type == 2:
                    displayEnemies ()
                    target[x] = enemy[int(input(f"Choose a target for {player[x].skillList[action[x]].name}: "))]
                if player[x].skillList[action[x]].type in [1,3]:
                    displayPlayers ()
                    target[x] = player[int(input(f"Choose a target for {player[x].skillList[action[x]].name}: "))]
                displayEnemies ()
                targetEx[x] = enemy[int(input(f"Choose a target for {player[x].skillList[0].name}: "))]
            else:
                displayEnemies ()
                target[x] = enemy[int(input(f"Choose a target for {player[x].skillList[action[x]].name}: "))]
                targetEx[x] = 0
        else:
            action[x] = 0
            target[x] = random.choice(listAliveCharacters(enemy))

# chooses enemy actions and targets
def enemyActions ():
    players = len(player)
    for x in range(1, len(enemy)+1):
        action[x+players] = random.choice(listActiveSkills(enemy[x]))
        if enemy[x].skillList[action[x+players]].type in [1]:
            target[x+players] = random.choice(listAliveCharacters(enemy))
        if enemy[x].skillList[action[x+players]].type in [3]:
            target[x+players] = random.choice(list(enemy.values()))
        if enemy[x].skillList[action[x+players]].type in [0,2,4]:
            target[x+players] = random.choice(listAliveCharacters(player))
        targetEx[x+players] = 0

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
    for x in range(1, len(enemy)+1):
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
            if slot[y].skillList[action[y]].cooldown == 0:
                time.sleep(0.2)
                useSkill(slot[y], action[y], target[y])
                slot[y].statUpdate ()
                target[y].statUpdate ()
                if targetEx[y] != 0:
                    time.sleep(0.2)
                    useBasicAttack (slot[y], targetEx[y])
                    slot[y].statUpdate ()
                    targetEx[y].statUpdate ()

    for x in range(1, len(slot)+1):
        slot[x].rotateStatChanges ()
        lowerSkillCooldown (slot[x])

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
        for x in range(1, len(enemy)+1):
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
        print(f"You Won! [{code}]")
    if enemyWon == True:
        print("You Lost...")
    input()