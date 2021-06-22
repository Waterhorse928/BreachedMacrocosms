import random
import charactersMaster

class Utsuho(charactersMaster.Character):
    basicAttackName = 'Control Rod Crush'
    def abyssNova(self, target):
        target.atkChange += self.mag
        target.magChange += self.mag
        target.resChange -= self.mag
        print(f'Utsuho uses Abyss Nova on {target.name}!')
        print (f'{target.name} gained {self.mag} ATK!')
        print (f'{target.name} gained {self.mag} MAG!')
        print (f'{target.name} lost {min(self.mag,target.res)} RES...')
    
class Orin(charactersMaster.Character):
    basicAttackName = "Kasha's Claws"
    def rekindlingOfDeadAshes(self, target):
        preHp = target.hp
        if target.hp is 0:
            target.hp = min(target.hp + (self.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + self.mag, target.maxHp)
        healed = target.hp - preHp
        print("Orin used Rekindling Of Dead Ashes!")
        print(f"{target.name} recovered {healed} HP!")
