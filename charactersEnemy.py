import random
import charactersMaster
import skillsList

class Rattata(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 15, 20, 0, 10, 20, 10, 15, 15, True, "Rattata")
        self.skillList.append(skillsList.BasicAttack(0,'Tackle'))
        self.skillList.append(skillsList.QuickAttack(1,"Quick Attack"))

class Zubat(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 10, 10, 10, 15, 15, 25, 10, 10, True, 'Zubat')
        self.skillList.append(skillsList.BasicAttack(0,'Bite'))
        self.skillList.append(skillsList.Supersonic(2,"Supersonic"))

class Muk(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 20, 10, 15, 10, 5, 5, 20, 20, True, 'Muk')
        self.skillList.append(skillsList.BasicAttack(0,'Pound'))
        self.skillList.append(skillsList.Sludge(2,"Sludge"))

class Pirate(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(1, 0, 15, 15, 15, 15, 15, 15, 15, 15, True, name)
        self.skillList.append(skillsList.BasicAttack(0,"Slash"))
        self.skillList.append(skillsList.WatchOut(2,"Watch Out"))
        self.skillList.append(skillsList.Shoot(2,"Shoot"))

class Beowolf(charactersMaster.Character):
    def __init__(self, name):
        super().__init__(1, 0, 15, 15, 15, 15, 15, 15, 15, 15, True, name)
        self.skillList.append(skillsList.BasicAttack(0,"Lunge"))
        self.skillList.append(skillsList.Supersonic(2,"Howl"))
        self.skillList.append(skillsList.Maul(2,"Maul"))

rocketCharacters = {0:"Team Rocket",1:Rattata(),2:Zubat(),3:Muk()}
beowolfCharacters = {0:"Beowolves",1:Beowolf("Beowolf A"),2:Beowolf("Beowolf B")}
pirateCharacters = {0:"Pirates",1:Pirate("Pirate A"),2:Pirate("Pirate B"),3:Pirate("Pirate C")}