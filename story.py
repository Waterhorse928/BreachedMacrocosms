def startStory (file, type):
    if type == 1:
        x = open(f"txt/{file}.txt","r",encoding='utf-8')
        y = x.read()
        print(y)
        input()

    if type == 2:
        x = open(f"txt/{file}.txt","r",encoding='utf-8')
        y = x.readlines()
        for z in y:
            print(z, end=' ')
            input()