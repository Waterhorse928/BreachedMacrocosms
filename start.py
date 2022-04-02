import battle
import charactersPlayer
import charactersEnemy
import story
import display

#Main Codes


#Volume 1 Codes

n0000 = ["Story2","Yukari1",2,["2468","1128","0803"],"0000"]# Choice: Utsuho, Nitori, or Suwako.

n2468 = ["Story","Utsuho1",2                                     ,"7417","2468"]# Utsuho Ch 1
n7417 = ["Fight",charactersPlayer.utsuho1,charactersEnemy.rocket1,"3939","7417"]# Utsuho Lvl 1
n3939 = ["Story","Utsuho2",2                                     ,"3846","3939"]# Utsuho Ch 2
n3846 = ["Fight",charactersPlayer.utsuho2,charactersEnemy.rocket2,"7726","3846"]# Utsuho Lvl 2
n7726 = ["Fight",charactersPlayer.utsuho3,charactersEnemy.rocket3,"4678","7726"]# Utsuho Lvl 3
n4678 = ["Story","Utsuho3",2                                     ,"8612","4678"]# Utsuho Ch 3

n1128 = ["Story","Nitori1",2                                     ,"9040","1128"]# Nitori Ch 1
n9040 = ["Fight",charactersPlayer.nitori1,charactersEnemy.pirate1,"3958","9040"]# Nitori Lvl 1
n3958 = ["Story","Nitori2",2                                     ,"3289","3958"]# Nitori Ch 2
n3289 = ["Fight",charactersPlayer.nitori2,charactersEnemy.pirate2,"0653","3289"]# Nitori Lvl 2
n0653 = ["Fight",charactersPlayer.nitori3,charactersEnemy.pirate3,"5382","0653"]# Nitori Lvl 3
n5382 = ["Story","Nitori3",2                                     ,"8612","5382"]# Nitori Ch 3

n0803 = ["Story","Suwako1",2                                      ,"0171","0803"]# Suwako Ch 1
n0171 = ["Fight",charactersPlayer.suwako1,charactersEnemy.beowolf1,"0804","0171"]# Suwako Lvl 1
n0804 = ["Story","Suwako2",2                                      ,"1606","0804"]# Suwako Ch 2
n1606 = ["Fight",charactersPlayer.suwako2,charactersEnemy.beowolf2,"3007","1606"]# Suwako Lvl 2
n3007 = ["Fight",charactersPlayer.suwako3,charactersEnemy.beowolf3,"0805","3007"]# Suwako Lvl 3
n0805 = ["Story","Suwako3",2                                      ,"8612","0805"]# Suwako Ch 3

#Volume 2 Codes

n8612 = ["Story2","Yukari2",2,["3196","4810","1894"],"8612"]# Choice: Mayumi, Komachi, or Aunn.

n3196 = ["Story","Mayumi1",2,"XXXX","3196"]# Mayumi Ch 1

n4810 = ["Story","Komachi1",2,"XXXX","4810"]# Komachi Ch 1

n1894 = ["Story","Aunn1",2,"XXXX","1894"]# Aunn Ch 1

#Test Codes

n2002 = ["Story","MarisaTest",2,"XXXX","2002"]# Marisa Test



def runCode (code):
    print (f"[Code:{code[4]}]")
    result = "repeat"
    if code[0] == "Fight":
        while result == "repeat":
            battle.playerList = code[1]
            battle.enemy = code[2]
            battle.code = f"Code:{code[3]}"
            result = battle.startBattle()        
    elif code[0] == "Story":
        result = story.startStory(code[1], 2)
    elif code[0] == "Story2":
        n = int(story.startStory(code[1], 3))
        code[3] = code[3][n-1]
    if result == "menu":
            code[3] = "MENU"
    return "n" + code[3]


while True:
    print ("1. Continue")
    print ("2. New")
    print ("3. Info")
    print ("0. Exit")
    select = int(input("Choose a number: "))
    
    if select == 2:
        nextCode = "n0000"
        while True:
            nextCode = runCode (eval(nextCode))
            if nextCode == "nXXXX":
                story.startStory("XXXX", 2)
                break

    if select == 3:
        displayCode = "n" + input("Enter code: ")
        display.displayCode(eval(displayCode))
    
    if select == 0:
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
        
        