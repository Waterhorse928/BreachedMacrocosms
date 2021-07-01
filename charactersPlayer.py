import random
import charactersMaster
import skillsList
import stats

class Gon(charactersMaster.Character):
    def __init__(self, level):
        data = stats.gon(level)
        super().__init__(1, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Gon")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Punch"))

class Layton(charactersMaster.Character):
    def __init__(self, level):
        data = stats.layton(level)
        super().__init__(1, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Layton")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Fencing"))

class Lea(charactersMaster.Character):
    def __init__(self, level):
        data = stats.lea(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Lea")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Chakram"))

class Marisa(charactersMaster.Character):
    def __init__(self, level):
        data = stats.marisa(level)
        super().__init__(1, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Marisa")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Broom Bash"))
            self.skillList.append(skillsList.MagicMissile(1,"Magic Missile"))

class Nitori(charactersMaster.Character):
    def __init__(self, level):
        data = stats.nitori(level)
        super().__init__(1, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Nitori")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Crowbar"))
            self.skillList.append(skillsList.OpticalCamouflage(1,"Optical Camouflage"))

class Orin(charactersMaster.Character):
    def __init__(self, level):
        data = stats.orin(level)
        super().__init__(1, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Orin")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Kasha's Claws"))
            self.skillList.append(skillsList.RekindlingOfDeadAshes(2,"Rekindling of Dead Ashes"))

class Sanae(charactersMaster.Character):
    def __init__(self, level):
        data = stats.sanae(level)
        super().__init__(2, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Sanae")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Gohei Smack"))
            self.skillList.append(skillsList.Heal(1,"Heal"))

class Suwako(charactersMaster.Character):
    def __init__(self, level):
        data = stats.suwako(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Suwako")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Iron Rings"))
            self.skillList.append(skillsList.Curse(1,"Curse"))

class Utsuho(charactersMaster.Character):
    def __init__(self, level):
        data = stats.utsuho(level)
        super().__init__(1, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Utsuho")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Control Rod Crush"))
            self.skillList.append(skillsList.AbyssNova(2,"Abyss Nova"))
    

tyCharacters1 = ["Ty",Utsuho(),Orin()]
beccaCharacters1 = ["Becca",Suwako(1),Sanae()]
mattCharacters1 = ["Matthew",Nitori(),Marisa()]