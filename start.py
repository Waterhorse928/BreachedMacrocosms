import battle
import charactersPlayer
import charactersEnemy
import story

while True:
    print ("1. Battle")
    print ("2. Story")
    print ("3. Codes")
#    print ("4. [WIP]")
    print ("4. Exit")
    select = int(input("Choose a number: "))
    
    if select == 1:
        fight = input("Enter code: ")
        if fight == "7417": # Utsuho Lvl 1
            battle.playerList = charactersPlayer.tyCharacters1
            battle.enemy = charactersEnemy.rocketCharacters
            battle.code = "Story Code: XXXX"
            battle.startBattle()    
            
        if fight == "9040": # Nitori Lvl 1
            battle.playerList = charactersPlayer.mattCharacters1
            battle.enemy = charactersEnemy.pirateCharacters
            battle.code = "Story Code: XXXX"
            battle.startBattle()
    
        if fight == "0171": # Suwako Lvl 1
            battle.playerList = charactersPlayer.beccaCharacters1
            battle.enemy = charactersEnemy.beowolfCharacters
            battle.code = "Story Code: 0804"
            battle.startBattle()
        
        if fight == "1606": # Suwako Lvl 2
            battle.playerList = charactersPlayer.suwako2
            battle.enemy = charactersEnemy.beowolves
            battle.code = "Battle Code: 3007"
            battle.startBattle()
        
        if fight == "3007": # Suwako Lvl 3
            battle.playerList = charactersPlayer.suwako3
            battle.enemy = charactersEnemy.beowolvesAlpha
            battle.code = "Story Code: XXXX"
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
    
#    if select == 4:
#        pass

    if select == 4:
        break