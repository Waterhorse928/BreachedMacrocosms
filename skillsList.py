import random

def multipleAttack(user, target):
    attackCount = 1
    if user.spd > target.spd:
        multipleAttackChance = user.spd - target.spd
        while multipleAttackChance > 1:
            multipleAttackCheck = random.randint(1, 100)
            if multipleAttackChance >= multipleAttackCheck:
                attackCount += 1
            else:
                break
            multipleAttackChance /= 2
    return attackCount

def crit(user, target):
    critMultiplier = 1
    if user.skl > target.luk:
        critChance = user.skl - target.luk
        while critChance > 1:
            critCheck = random.randint(1, 100)
            if critChance >= critCheck:
                critMultiplier += 0.5
            else:
                break
            critChance /= 2
    return critMultiplier

def miss(user, target):
    miss = False
    if user.skl < target.luk:
        missChance = (target.luk * 2) - (user.skl * 2)
        missCheck = random.randint(1, 100)
        if missChance >= missCheck:
            miss = True
    return miss

class Skill:
    def __init__(self, type, cooldown, name):
        self.type = type
        self.cooldown = cooldown
        self.maxCooldown = cooldown
        self.name = name

class BasicAttack (Skill):
    def __init__(self, name):
        super().__init__(0, 0, name)
    
    def skill(self, user, target):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = round((user.atk * 2 * critMod) - target.dfn)
        print(f"{user.name} used {self.name}!")
        if atkCount != 1:
            print(f"{user.name} attacked {atkCount} times!")
        if critMod != 1:
            print(f"x{critMod} Critical!")
        for i in range(atkCount):
            if miss(user, target) == False:
                target.hp -= atkDmg
                print(f"{target.name} takes {atkDmg} Damage!")
            else:
                print(f"{target.name} dodged...")

class AbyssNova (Skill):
    def __init__(self):
        super().__init__(0, 2, "Abyss Nova")
    
    def skill(self, user, target):
        target.atkChange += user.mag
        target.magChange += user.mag
        target.resChange -= user.mag
        print(f'{user.name} used Abyss Nova!')
        print (f'{target.name} gained {user.mag} ATK!')
        print (f'{target.name} gained {user.mag} MAG!')
        print (f'{target.name} lost {min(user.mag,target.res)} RES...')

class RekindlingOfDeadAshes (Skill):
    def __init__(self):
        super().__init__(1, 2, "Rekindling of Dead Ashes")
    
    def rekindlingOfDeadAshes(self, user, target):
        preHp = target.hp
        if target.hp == 0:
            target.hp = min(target.hp + (user.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + user.mag, target.maxHp)
        healed = target.hp - preHp
        print(f"{user.name} used Rekindling Of Dead Ashes!")
        print(f"{target.name} recovered {healed} HP!")

class Supersonic (Skill):
    def __init__(self):
        super().__init__(type, 2, "Supersonic")
    
    def supersonic(self, user, target):
        target.atkChange -= user.atk
        print(f'{user.name} uses Supersonic on {target.name}!')
        print(f'{target.name} lost {min(user.atk, target.atk)} ATK...')
