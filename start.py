import battle
import charactersPlayer
import charactersEnemy
import story

while True:
    print ("1. Battle")
    print ("2. Story")
    print ("3. Codes")
    print ("4. Stats [WIP]")
    print ("5. Exit")
    select = int(input("Choose a number: "))
    
    if select == 1:
        fight = input("Enter code: ")
        if fight == "7417":
            battle.playerList = charactersPlayer.tyCharacters1
            battle.enemy = charactersEnemy.rocketCharacters
            battle.code = "XXXX"
            battle.startBattle()
    
        if fight == "9040":
            battle.playerList = charactersPlayer.mattCharacters1
            battle.enemy = charactersEnemy.pirateCharacters
            battle.code = "XXXX"
            battle.startBattle()
    
        if fight == "0171":
            battle.playerList = charactersPlayer.beccaCharacters1
            battle.enemy = charactersEnemy.beowolfCharacters
            battle.code = "0804"
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
        story.startStory("Codes", 1)
    
    if select == 4:
        pass

    if select == 5:
        break