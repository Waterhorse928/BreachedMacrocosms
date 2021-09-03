import battle
import charactersPlayer
import charactersEnemy
import story
import display

n7417 = ["Fight",charactersPlayer.utsuho1,charactersEnemy.rocket1,"3939","7417"]# Utsuho Lvl 1
n3846 = ["Fight",charactersPlayer.utsuho2,charactersEnemy.rocket2,"7726","3846"]# Utsuho Lvl 2
n7726 = ["Fight",charactersPlayer.utsuho3,charactersEnemy.rocket3,"4678","7726"]# Utsuho Lvl 3
n9040 = ["Fight",charactersPlayer.nitori1,charactersEnemy.pirate1,"3958","9040"]# Nitori Lvl 1
n3289 = ["Fight",charactersPlayer.nitori2,charactersEnemy.pirate2,"0653","3289"]# Nitori Lvl 2
n0653 = ["Fight",charactersPlayer.nitori3,charactersEnemy.pirate3,"XXXX","0653"]# Nitori Lvl 3
n0171 = ["Fight",charactersPlayer.suwako1,charactersEnemy.beowolf1,"0804","0171"]# Suwako Lvl 1
n1606 = ["Fight",charactersPlayer.suwako2,charactersEnemy.beowolf2,"3007","1606"]# Suwako Lvl 2
n3007 = ["Fight",charactersPlayer.suwako3,charactersEnemy.beowolf3,"XXXX","3007"]# Suwako Lvl 3
n2468 = ["Story","Utsuho1",2,"7417","2468"]# Utsuho Ch 1
n3939 = ["Story","Utsuho2",2,"3846","3939"]# Utsuho Ch 2
n4678 = ["Story","Utsuho3",2,"XXXX","4678"]# Utsuho Ch 3
n1128 = ["Story","Nitori1",2,"9040","1128"]# Nitori Ch 1
n3958 = ["Story","Nitori2",2,"3289","3958"]# Nitori Ch 2
n0803 = ["Story","Suwako1",2,"0171","0803"]# Suwako Ch 1
n0804 = ["Story","Suwako2",2,"XXXX","0804"]# Suwako Ch 2
n2002 = ["Story","MarisaTest",2,"XXXX","2002"]# Marisa Test
n0000 = ["Story2","Yukari",2,["2468","1128","0803"],"0000"]# Choice


def runCode (code):
    print (f"[Code:{code[4]}]")
    result = "repeat"
    if code[0] == "Fight":
        t = 1
    if code[0] == "Story":
        t = 2
    if code[0] == "Story2":
        t = 3
    if t == 1:
        while result == "repeat":
            battle.playerList = code[1]
            battle.enemy = code[2]
            battle.code = f"Code:{code[3]}"
            result = battle.startBattle()        
    if t == 2:
        result = story.startStory(code[1], 2)
    if t == 3:
        n = int(story.startStory(code[1], 3))
        code[3] = code[3][n-1]
    if result == "menu":
            code[3] = "MENU"
    return "n" + code[3]


while True:
    print ("1. Continue")
    print ("2. New")
    print ("3. Exit")
    select = int(input("Choose a number: "))
    
    if select == 2:
        nextCode = "n0000"
        while True:
            nextCode = runCode (eval(nextCode))
            if nextCode == "nXXXX":
                story.startStory("XXXX", 2)
                break

    if select == 4:
        display.displayCode(n7726)
    
    if select == 3:
        break

    if select == 1:
        nextCode = "n" + input("Enter code: ")
        while True:
            nextCode = runCode (eval(nextCode))
            if nextCode == "nXXXX":
                story.startStory("XXXX", 2)
                break
            if nextCode == "nMENU":
                break
        
        