import story

def displayCode(code):
    playerlist = {}
    for z in range(1, len(code[1])):
        playerlist[z]=code[1][z]
    code[1] = playerlist
    while True:
        print("--Teams--")
        print(" 1. Player")
        print(" 2. Foe")
        print(" 0. Back")
        x = int(input("Choose a number: "))
        if x == 0:
            break
        while True:
            print("--Characters--")
            for y in range(1, len(code[x]) + 1):
                print(f" {y}. {code[x][y].name}")
            print(" 0. Back")
            a = int(input("Choose a number: "))
            if a == 0:
                break
            displayCharacter(code[x][a])

def displayCharacter(char):
    while True:
        print(f"--{char.name}--")
        print(" 1. Stats")
        print(" 2. Skills")
        print(" 0. Back")
        b = int(input("Choose a number: "))
        if b == 0:
            break
        if b == 1:
            print(f"--{char.name}-- [{char.hp}/{char.maxHp}] HP")
            print(f"VIT: {char.vit}")
            print(f"ATK: {char.atk}")
            print(f"MAG: {char.mag}")
            print(f"SKL: {char.skl}")
            print(f"SPD: {char.spd}")
            print(f"LUK: {char.luk}")
            print(f"DEF: {char.dfn}")
            print(f"RES: {char.res}")
            input()
        if b == 2:
            while True:
                print(f"--{char.name}'s Skills--")
                for d in range(0, len(char.skillList)):
                   print(f" {d+1}. {char.skillList[d].name}")
                print(" 0. Back")
                c = int(input("Choose a number: "))
                if c == 0:
                    break
                story.startStory(char.skillList[c-1].name, 4)
