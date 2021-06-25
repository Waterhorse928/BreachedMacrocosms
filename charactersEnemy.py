import random
import charactersMaster
import skillsList

class Rattata(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 15, 20, 0, 10, 20, 10, 15, 15, True, "Rattata")
        self.skillList.append(skillsList.BasicAttack('Tackle'))
        self.skillList.append(skillsList.QuickAttack())

class Zubat(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 10, 10, 10, 15, 15, 25, 10, 10, True, 'Zubat')
        self.skillList.append(skillsList.BasicAttack('Bite'))
        self.skillList.append(skillsList.Supersonic())

class Muk(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 20, 10, 15, 10, 5, 5, 20, 20, True, 'Muk')
        self.skillList.append(skillsList.BasicAttack('Pound'))
        self.skillList.append(skillsList.Sludge())

rocketCharacters = {0:"Team Rocket",1:Rattata(),2:Zubat(),3:Muk()}