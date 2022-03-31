import os
import skillsInfo
dir_path = os.path.dirname(os.path.abspath(__file__))
def startStory (file, type):
    if type == 1:
        x = open(f"{dir_path}/txt/story/{file}.txt","r",encoding='utf-8')
        y = x.read()
        print(y)
        input()
        return 2

    if type == 2:
        x = open(f"{dir_path}/txt/story/{file}.txt","r",encoding='utf-8')
        y = x.readlines()
        for z in y:
            z = z.replace("\n","")
            print(z, end='')
            a = input(" ")
            if a == "skip":
                return "next"
            if a == "menu":
                return "menu"

    if type == 3:
        x = open(f"{dir_path}/txt/story/{file}.txt","r",encoding='utf-8')
        y = x.readlines()
        for z in y:
            z = z.replace("\n","")
            z = z.replace("~!@","\n")
            print(z, end='')
            a = input(" ")
            if a == "skip":
                break
        return input ("Choose a number: ")

    if type == 4:
        # Old File Based System
        #x = open(f"{dir_path}/txt/skills/{file}.txt","r",encoding='utf-8')
        #y = x.read()
        y = skillsInfo.getSkillInfo(file)
        print(y)
        input()
