import battle
import charactersPlayer
import charactersEnemy

print ("1. Battle")
select = int(input("What would you like to do?: "))

if select == 1:
    fight = int(input("Enter code: "))
    if fight == 7417:
        battle.playerList = charactersPlayer.tyCharacters
        battle.enemy = charactersEnemy.rocketCharacters
        battle.startBattle()

    if fight == 9040:
        battle.playerList = charactersPlayer.mattCharacters
        battle.enemy = charactersEnemy.rocketCharacters
        battle.startBattle()

    if fight == 2171:
        battle.playerList = charactersPlayer.beccaCharacters
        battle.enemy = charactersEnemy.beowolfCharacters
        battle.startBattle()


if select == 2:
    pass

if select == 3:
    pass
