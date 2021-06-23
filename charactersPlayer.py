import random
import charactersMaster

class Utsuho(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 27, 29, 32, 12, 2, 4, 28, 26, False, "Utsuho")
        self.atkName = 'Control Rod Crush'
         
    def abyssNova(self, target):
        target.atkChange += self.mag
        target.magChange += self.mag
        target.resChange -= self.mag
        print(f'Utsuho uses Abyss Nova on {target.name}!')
        print (f'{target.name} gained {self.mag} ATK!')
        print (f'{target.name} gained {self.mag} MAG!')
        print (f'{target.name} lost {min(self.mag,target.res)} RES...')
    
class Orin(charactersMaster.Character):
    def __init__(self, level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name):
        super().__init__(level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name)
        self.atkName = "Kasha's Claws"
    def rekindlingOfDeadAshes(self, target):
        preHp = target.hp
        if target.hp == 0:
            target.hp = min(target.hp + (self.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + self.mag, target.maxHp)
        healed = target.hp - preHp
        print(f"Orin used Rekindling Of Dead Ashes on {target.name}!")
        print(f"{target.name} recovered {healed} HP!")
