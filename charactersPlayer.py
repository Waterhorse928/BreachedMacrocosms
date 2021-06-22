import random
import charactersMaster

class Utsuho(charactersMaster.Character):
    basicAttackName = 'Control Rod Crush'
    def abyssNova(self, target):
        target.atkChange += self.mag
        target.magChange += self.mag
        target.resChange -= self.mag
        print('Abyss Nova function run')
    
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
