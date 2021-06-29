import battle
import charactersPlayer
import charactersEnemy
import story

print ("1. Battle")
print ("2. Story")
select = int(input("Choose a number: "))

if select == 1:
    fight = input("Enter code: ")
    if fight == "7417":
        battle.playerList = charactersPlayer.tyCharacters
        battle.enemy = charactersEnemy.rocketCharacters
        battle.startBattle()

    if fight == "9040":
        battle.playerList = charactersPlayer.mattCharacters
        battle.enemy = charactersEnemy.pirateCharacters
        battle.startBattle()

    if fight == "0171":
        battle.playerList = charactersPlayer.beccaCharacters
        battle.enemy = charactersEnemy.beowolfCharacters
        battle.startBattle()

if select == 2:
    script = input("Enter code: ")
    print ("1. Wall o' Text")
    print ("2. Line by Line")
    type = int(input ('Choose a format: '))
    if script == "2468":
        story.startStory("Utsuho1", type)
    if script == "1128":
        story.startStory("Nitori1", type)
    if script == "0803":
        story.startStory("Suwako1", type)
    if script == "0804":
        story.startStory("Suwako2", type)
    if script == "2002":
        story.startStory("MarisaTest", type)

if select == 3:
    pass
