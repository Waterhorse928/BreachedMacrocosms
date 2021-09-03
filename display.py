def displayCode(code):
    for z in range(1, len(code[1])):
        playerlist = dict.fromkeys(str(z), code[1][z])
    code[1] = playerlist
    while True:
        print("1. Player")
        print("2. Foe")
        print("0. Back")
        x = int(input("Choose a number: "))
        if x == 0:
            break
        while True:
            for y in range(1, len(code[x]) + 1):
                print(f"{y}. {code[x][y].name}")
            print("0. Back")
            a = input("Choose a number: ")
            if a == 0:
                break
            displayCharacter(code[x][a])

def displayCharacter(char):
    while True:
        print("1. Stats")
        print("2. Skills")
        print("0. Back")
        b = input("Choose a number: ")
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
        if b == 2:
            while True:
                for x in range(0, len(char.skillList)):
                   print(f"{x+1}. {char.skillList[x].name}")
                break
