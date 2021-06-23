import math
import random
import charactersPlayer
import charactersEnemy

# Character Lists
playerList = charactersPlayer.tyCharacters
player = {}
enemy = charactersEnemy.rocketCharacters

# Displays enemies and sets up enemy party
def encounter ():
    print(f"Encountered {enemy[0]}!")
    print(end="  ")
    for x in range(1, len(enemy)-1):
        print(f"{enemy[x].name},", end=' ')
    print(f"and {enemy[int(len(enemy)-1)].name}!")

# Displays player's characters and asks them to choose a party
def characterSelect ():
    print(f"{playerList[0]}'s Characters:")
    for x in range(1, len(playerList)):
        print(f" {x}. {playerList[x].name}")

    for x in range(1, min(len(playerList), 5)):
        player[int(x)] = input(f"Choose a character for slot {x}: ")
        player[int(x)] = int(player[int(x)])
        player[int(x)] = playerList[player[int(x)]]

# Displays skills for a particular character
def listSkills ():
    print(f"{player[1].name}'s Skills:")
    for x in range(len(player[1].skillList)):
        print(f" {x}. {player[1].skillList[x].name}")

# Use a skill. Not working yet.
def useSkill(user, skill, target):
    player[user].skillList[skill].skill(player[user],player[target])

encounter ()
