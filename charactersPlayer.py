import random
import charactersMaster
import skillsList

class Utsuho(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 27, 29, 32, 12, 2, 4, 28, 26, False, "Utsuho")
        self.skillList.append(skillsList.BasicAttack("Control Rod Crush"))
        self.skillList.append(skillsList.AbyssNova())
    
class Orin(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 16, 17, 22, 19, 32, 29, 10, 15, False, "Orin")
        self.skillList.append(skillsList.BasicAttack("Kasha's Claws"))
        self.skillList.append(skillsList.RekindlingOfDeadAshes())

tyCharacters = ["Ty's Characters",Utsuho(),Orin()]