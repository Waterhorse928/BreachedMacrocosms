import os
dir_path = os.path.dirname(os.path.abspath(__file__))
def startStory (file, type):
    if type == 1:
        x = open(f"{dir_path}/txt/{file}.txt","r",encoding='utf-8')
        y = x.read()
        print(y)
        input()

    if type == 2:
        x = open(f"{dir_path}/txt/{file}.txt","r",encoding='utf-8')
        y = x.readlines()
        for z in y:
            z = z.replace("\n","")
            print(z, end='')
            a = input(" ")
            if a == "skip":
                break