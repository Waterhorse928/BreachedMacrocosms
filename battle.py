import math
import random
import charactersPlayer
import charactersEnemy
import skillsList
import discord
from discord.ext.commands import Bot
bot = skillsList.bot
TOKEN = 'ODU4MDMxMjI3Mjk3NzI2NTA0.YNYN2g.Y7NiBR--GboIfHKX1IiW-ZWJCLY'

@bot.event
async def on_ready():
    await bot.get_channel(858035586564751390).send(f'Bot connected as {bot.user}')
    
	
@bot.event
async def on_message(message):
    if message.content == 'test':
	    await message.channel.send('Testing 1 2 3!')
    await bot.process_commands(message)
    
@bot.command(name='bm')
async def beginBattle(context):
    await startBattle()
    await bot.process_commands(context)

  

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
targetEx = {}

channel = bot.get_channel(858035586564751390)

# Displays enemies at the start and removes enemy[0]
async def encounter ():
    channel = bot.get_channel(858035586564751390)
    await channel.send(f"Encountered {enemy[0]}!")
    for x in range(1, len(enemy)-1):
        await channel.send(f"{enemy[x].name},")
    await channel.send(f"and {enemy[int(len(enemy)-1)].name}!")
    del enemy[0]
 
# displays enemies for selection. Only alive ones
async def displayEnemies ():
    channel = bot.get_channel(858035586564751390)
    for x in range(1, len(enemy)+1):
        if enemy[x].isAlive == True:
            await channel.send(f" {x}. {enemy[x].name}")

# Returns a list of alive characters, player or enemy
def listAliveCharacters (dict):
    aliveList = []
    for x in range(1, len(dict)+1):
        if dict[x].isAlive == True:
            aliveList.append(dict[x])
    if aliveList == []:
        aliveList = [0]
    return aliveList

# Returns a list of useable skills
def listActiveSkills (user):
    activeSkills = []
    for x in range(0, len(user.skillList)):
        if user.skillList[x].cooldown == 0:
            activeSkills.append(x)
    return activeSkills

# lowers skill cooldowns by 1
async def lowerSkillCooldown (user):
    for x in user.skillList:
        if x.cooldown != 0:
            x.cooldown -= 1

# Displays player's characters and asks them to choose a party
async def characterSelect ():
    channel = bot.get_channel(858035586564751390)
    await channel.send(f"{playerList[0]}'s Characters:")
    for x in range(1, len(playerList)):
        await channel.send(f" {x}. {playerList[x].name}")

    for x in range(1, min(len(playerList), 5)):
        await channel.send(f"Choose a character for slot {x}: ")
        async def on_message(message):
            player[x] = await bot.wait_for("message") #WWWWWWWWWWWWWWWWWWHHHHHHHHHHHHHHHHHHHHHHHHHHHYYYYYYYYYYYYYYYYYYYYYYYYY
            print(player[x])
            player[x] = int(player[x])
            player[x] = playerList[player[x]]

# Displays player's slots
async def displayPlayers ():
    channel = bot.get_channel(858035586564751390)
    for x in range(1, len(player)+1):
        await channel.send(f" {x}. {player[x].name}")

# Displays skills for a particular character
async def listSkills (user):
    channel = bot.get_channel(858035586564751390)
    await channel.send(f"{user.name}'s Skills:")
    for x in range(len(user.skillList)):
        if user.skillList[x].cooldown == 0:
            await channel.send(f" {x}. {user.skillList[x].name}")
        else:
            if user.skillList[x].cooldown == 1:
                turns = "turn"
            else:
                turns = "turns"
            await channel.send(f" X. {user.skillList[x].name} [Cooldown: {user.skillList[x].cooldown} {turns}]")

# Use a skill.
async def useSkill(user, skill, target):
    if target in player.values():
        party = player
    if target in enemy.values():
        party = enemy
    party = listAliveCharacters(party)
    if user.skillList[skill].type in [0,1,2]:
        if target.hp == 0:
            if target in player.values():
                target = random.choice(listAliveCharacters(player))
            if target in enemy.values():
                target = random.choice(listAliveCharacters(enemy))
    if target != [0]:
        await user.skillList[skill].skill(user,target,party)

# use Basic Attack
async def useBasicAttack (user, target):
    if target in player.values():
        party = player
    if target in enemy.values():
        party = enemy
    party = listAliveCharacters(party)
    if target.hp == 0:
            if target in player.values():
                target = random.choice(listAliveCharacters(player))
            if target in enemy.values():
                target = random.choice(listAliveCharacters(enemy))
    await user.skillList[0].skill(user,target,party)

# choose actions loop
async def chooseActions ():
    for x in range(1, len(player)+1):
        if player[x].isAlive == True:
            await listSkills (player[x])
            action[x] = int(input("Choose a skill: "))
            if player[x].skillList[action[x]].type == 1 or player[x].skillList[action[x]].type == 3:
                await displayPlayers ()
                target[x] = player[int(input("Choose a target for skill: "))]
                await displayEnemies ()
                targetEx[x] = enemy[int(input("Choose a target for extra attack: "))]
            else:
                await displayEnemies ()
                target[x] = enemy[int(input("Choose a target for skill: "))]
                targetEx[x] = 0
        else:
            action[x] = 0
            target[x] = random.choice(listAliveCharacters(enemy))

# chooses enemy actions and targets
def enemyActions ():
    players = len(player)
    for x in range(1, len(enemy)+1):
        action[x+players] = random.choice(listActiveSkills(enemy[x]))
        targetEx[x+players] = 0
        target[x+players] = random.choice(listAliveCharacters(player))

# Helps turnOrder sort or something
def turnKey(self):
    return self.turnNumber

# redefines turnList, slotList and slot
async def turnOrder ():
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
async def round ():
    channel = bot.get_channel(858035586564751390)
    for x in range(0, len(turnList)):
        y = slotList.index(turnList[x])+1
        slot[y].statUpdate ()
        target[y].statUpdate ()
        if slot[y].isAlive == True:
            if slot[y].skillList[action[y]].cooldown == 0:
                await useSkill(slot[y], action[y], target[y])
                slot[y].statUpdate ()
                target[y].statUpdate ()
                if target[y].hp == 0:
                    await channel.send(f"{target[y].name} was knocked out!")
                if targetEx[y] != 0:
                    await useBasicAttack (slot[y], targetEx[y])
                    slot[y].statUpdate ()
                    targetEx[y].statUpdate ()
                    if targetEx[y].hp == 0:
                        await channel.send(f"{targetEx[y].name} was knocked out!")

    for x in range(1, len(slot)+1):
        slot[x].rotateStatChanges ()
        await lowerSkillCooldown (slot[x])

# run the entire battle
async def startBattle ():
    channel = bot.get_channel(858035586564751390)
    await encounter ()
    await characterSelect ()
    battleOver = False
    playerWon = False
    enemyWon = False
    while battleOver == False:
        await chooseActions ()
        await turnOrder ()
        enemyActions ()
        await round ()
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
        await channel.send("You Won!")
    if enemyWon == True:
        await channel.send("You Lost...")

bot.run(TOKEN)