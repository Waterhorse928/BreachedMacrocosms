import battle
import charactersPlayer
import charactersEnemy
import story

n7417 = ["Fight",charactersPlayer.utsuho1,charactersEnemy.rocket1,"3939","7417"]# Utsuho Lvl 1
n3846 = ["Fight",charactersPlayer.utsuho2,charactersEnemy.rocket2,"7726","3846"]# Utsuho Lvl 2
n7726 = ["Fight",charactersPlayer.utsuho3,charactersEnemy.rocket3,"XXXX","7726"]# Utsuho Lvl 3
n9040 = ["Fight",charactersPlayer.nitori1,charactersEnemy.pirate1,"3958","9040"]# Nitori Lvl 1
#n3289 = ["Fight",charactersPlayer.nitori2,charactersEnemy.pirate2,"0653","3289"]# Nitori Lvl 2
#n0653 = ["Fight",charactersPlayer.nitori3,charactersEnemy.pirate3,"XXXX","0653"]# Nitori Lvl 3
n0171 = ["Fight",charactersPlayer.suwako1,charactersEnemy.beowolf1,"0804","0171"]# Suwako Lvl 1
n1606 = ["Fight",charactersPlayer.suwako2,charactersEnemy.beowolf2,"3007","1606"]# Suwako Lvl 2
n3007 = ["Fight",charactersPlayer.suwako3,charactersEnemy.beowolf3,"XXXX","3007"]# Suwako Lvl 3
n2468 = ["Story","Utsuho1",2,"7417","2468"]# Utsuho Chap 1
n3939 = ["Story","Utsuho2",2,"3846","3939"]# Utsuho Chap 2
n1128 = ["Story","Nitori1",2,"9040","1128"]# Nitori Chap 1
n3958 = ["Story","Nitori2",2,"XXXX","3958"]# Nitori Chap 2
n0803 = ["Story","Suwako1",2,"0171","0803"]# Suwako Chap 1
n0804 = ["Story","Suwako2",2,"XXXX","0804"]# Suwako Chap 2
n2002 = ["Story","MarisaTest",2,"XXXX","2002"]# Marisa Test


def runCode (code):
    print (f"[Code:{code[4]}]")
    if code[0] == "Fight":
        t = 1
    if code[0] == "Story":
        t = 2
    if t == 1:
        battle.playerList = code[1]
        battle.enemy = code[2]
        battle.code = f"Code:{code[3]}"
        battle.startBattle()
    if t == 2:
        story.startStory(code[1], 2)
    return "n" + code[3]


while True:
    print ("1. Continue")
    print ("2. New")
    print ("3. Codes")
    print ("4. Exit")
    select = int(input("Choose a number: "))
    
    if select == 2:
        pass

    if select == 3:
        story.startStory("Codes", 1)
    
    if select == 4:
        break

    if select == 1:
        nextCode = "n" + input("Enter code: ")
        while True:
            nextCode = runCode (eval(nextCode))
            if nextCode == "nXXXX":
                story.startStory("XXXX", 2)
                break
        
        