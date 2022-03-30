import random
import charactersMaster
import skillsList
import stats

class Gon(charactersMaster.Character):
    def __init__(self, level):
        data = stats.gon(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Gon")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Punch"))
            self.skillList.append(skillsList.ShowMeRock(1,"Show Me Rock!"))
        if level >= 3:
            self.skillList.append(skillsList.Maul(2,"Janken Rock!"))

class Layton(charactersMaster.Character):
    def __init__(self, level):
        data = stats.layton(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Layton")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Fencing"))
            self.skillList.append(skillsList.Thinking(1,"Critical Thinking"))
        if level >= 3:
            self.skillList.append(skillsList.Shoot(1,"Calculated Strike"))

class Lea(charactersMaster.Character):
    def __init__(self, level):
        data = stats.lea(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Lea")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Chakram"))
            self.skillList.append(skillsList.Heat(2, "Heat Element"))
        if level >= 3:
            self.skillList.append(skillsList.BlazingDragon(3, "Blazing Dragon"))

class Marisa(charactersMaster.Character):
    def __init__(self, level):
        data = stats.marisa(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Marisa")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Broom Bash"))
            self.skillList.append(skillsList.MagicMissile(1,"Magic Missile"))
        if level >= 3:
            self.skillList.append(skillsList.Sludge(2,"Non-Directional Laser"))

class Nitori(charactersMaster.Character):
    def __init__(self, level):
        data = stats.nitori(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Nitori")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Crowbar"))
            self.skillList.append(skillsList.Repair(3,"Repair"))
        if level >= 3:
            self.skillList.append(skillsList.PhotonTorpedo(2,"Photon Torpedo"))
        if level >= 5:
            self.skillList.append(skillsList.OpticalCamouflage(1,"Optical Camouflage"))

class Orin(charactersMaster.Character):
    def __init__(self, level):
        data = stats.orin(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Orin")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Kasha's Claws"))
            self.skillList.append(skillsList.RekindlingOfDeadAshes(2,"Rekindling of Dead Ashes"))
        if level >= 3:
            self.skillList.append(skillsList.CatsWalk(3,"Cat's Walk"))

class Ruby(charactersMaster.Character):
    def __init__(self, level):
        data = stats.ruby(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Ruby")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0, "Crescent Rose"))
            self.skillList.append(skillsList.Speed(1,"Speed"))
        if level >= 3:
            self.skillList.append(skillsList.Rush(2,"High-Speed Rush"))
        
class Sanae(charactersMaster.Character):
    def __init__(self, level):
        data = stats.sanae(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Sanae")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Gohei Smack"))
            self.skillList.append(skillsList.Heal(1,"Heal"))
        if level >= 3:
            self.skillList.append(skillsList.Miracle(1,"Miracle"))

class Suwako(charactersMaster.Character):
    def __init__(self, level):
        data = stats.suwako(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Suwako")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Iron Rings"))
            self.skillList.append(skillsList.GeyserColumn(1,"Geyser"))            
        if level >= 3:
            self.skillList.append(skillsList.Curse(1,"Curse"))

class Utsuho(charactersMaster.Character):
    def __init__(self, level):
        data = stats.utsuho(level)
        super().__init__(level, 0, data["vit"], data["atk"], data["mag"], data["skl"], data["spd"], data["luk"], data["dfn"], data["res"], False, "Utsuho")
        if level >= 1:
            self.skillList.append(skillsList.BasicAttack(0,"Control Rod Crush"))
            self.skillList.append(skillsList.AbyssNova(2,"Abyss Nova"))
        if level >= 3:
            self.skillList.append(skillsList.Sun(4,"Subterranean Sun"))
    
utsuho1 = [" ",Utsuho(1),Orin(1)]
utsuho2 = [" ",Utsuho(2),Orin(2),Lea(2)]
utsuho3 = [" ",Utsuho(3),Orin(3),Lea(3)]
nitori1 = [" ",Nitori(1),Marisa(1)]
nitori2 = [" ",Nitori(2),Marisa(2),Ruby(2)]
nitori3 = [" ",Nitori(3),Marisa(3),Ruby(3)]
suwako1 = [" ",Suwako(1),Sanae(1)]
suwako2 = [" ",Suwako(2),Sanae(2),Layton(2)]
suwako3 = [" ",Suwako(3),Sanae(3),Layton(3)]