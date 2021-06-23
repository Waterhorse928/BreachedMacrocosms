import random
import charactersMaster

class Skill:
    def __init__(self, type, cooldown, maxCooldown, name):
        self.type = type
        self.cooldown = cooldown
        self.maxCooldown = maxCooldown
        self.name = name


class BasicAttack (Skill):
    def __init__(self, name):
        super().__init__(0, 0, 0, name)
    
    def skill(self, user, target):
        critMod = charactersMaster.crit(user, target)
        atkCount = charactersMaster.multipleAttack(user, target)
        atkDmg = round((user.atk * 2 * critMod) - target.dfn)
        print(f"{user.name} uses {user.atkName} on {target.name}!")
        if atkCount != 1:
            print(f"{user.name} attacks {atkCount} times!")
        if critMod != 1:
            print(f"x{critMod} Critical!")
        for i in range(atkCount):
            if charactersMaster.miss(user, target) == False:
                target.hp -= atkDmg
                print(f"{target.name} takes {atkDmg} Damage!")
            else:
                print(f"{target.name} dodged...")

class AbyssNova (Skill):
    def __init__(self):
        super().__init__(0, 2, 2, "Abyss Nova")
    
    def skill(self, user, target):
        target.atkChange += user.mag
        target.magChange += user.mag
        target.resChange -= user.mag
        print(f'{user.name} uses Abyss Nova on {target.name}!')
        print (f'{target.name} gained {user.mag} ATK!')
        print (f'{target.name} gained {user.mag} MAG!')
        print (f'{target.name} lost {min(user.mag,target.res)} RES...')

class RekindlingOfDeadAshes (Skill):
    def __init__(self):
        super().__init__(1, 2, 2, "Rekindling of Dead Ashes")
    
    def rekindlingOfDeadAshes(self, user, target):
        preHp = target.hp
        if target.hp == 0:
            target.hp = min(target.hp + (user.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + user.mag, target.maxHp)
        healed = target.hp - preHp
        print(f"{user.name} used Rekindling Of Dead Ashes on {target.name}!")
        print(f"{target.name} recovered {healed} HP!")