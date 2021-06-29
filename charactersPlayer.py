import random
import charactersMaster
import skillsList

class Utsuho(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 27, 29, 32, 12, 2, 4, 28, 26, False, "Utsuho")
        self.skillList.append(skillsList.BasicAttack(0,"Control Rod Crush"))
        self.skillList.append(skillsList.AbyssNova(2,"Abyss Nova"))
    
class Orin(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 16, 17, 22, 19, 32, 29, 10, 15, False, "Orin")
        self.skillList.append(skillsList.BasicAttack(0,"Kasha's Claws"))
        self.skillList.append(skillsList.RekindlingOfDeadAshes(2,"Rekindling of Dead Ashes"))

class Marisa(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 18, 17, 30, 20, 25, 13, 15, 22, False, "Marisa")
        self.skillList.append(skillsList.BasicAttack(0,"Broom Bash"))
        self.skillList.append(skillsList.MagicMissile(1,"Magic Missile"))

class Lea(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 20, 20, 20, 20, 20, 20, 20, 20, False, "Lea")
        self.skillList.append(skillsList.BasicAttack(0,"Chakram"))

class Suwako(charactersMaster.Character):
    def __init__(self):
        super().__init__(2, 0, 16, 18, 25, 26, 17, 25, 16, 23, False, "Suwako")
        self.skillList.append(skillsList.BasicAttack(0,"Iron Rings"))
        self.skillList.append(skillsList.Curse(1,"Curse"))

class Sanae(charactersMaster.Character):
    def __init__(self):
        super().__init__(2, 0, 23, 10, 17, 14, 19, 31, 26, 27, False, "Sanae")
        self.skillList.append(skillsList.BasicAttack(0,"Gohei Smack"))
        self.skillList.append(skillsList.Heal(1,"Heal"))

class Nitori(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 19, 27, 7, 26, 22, 24, 18, 17, False, "Nitori")
        self.skillList.append(skillsList.BasicAttack(0,"Crowbar"))
        self.skillList.append(skillsList.OpticalCamouflage(1,"Optical Camouflage"))

class Layton(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 26, 22, 4, 29, 22, 16, 22, 19, False, "Layton")
        self.skillList.append(skillsList.BasicAttack(0,"Fencing"))

class Gon(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 28, 29, 0, 23, 28, 21, 27, 4, False, "Gon")
        self.skillList.append(skillsList.BasicAttack(0,"Punch"))

tyCharacters = ["Ty",Utsuho(),Orin()]
beccaCharacters = ["Becca",Suwako(),Sanae()]
mattCharacters = ["Matthew",Nitori(),Marisa()]