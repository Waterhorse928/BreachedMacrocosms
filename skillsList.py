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
        self.cooldown = 0
        self.maxCooldown = cooldown
        self.name = name

class BasicAttack (Skill):
    def __init__(self, name):
        super().__init__(0, 0, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 2 * critMod) - target.dfn),0)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for i in range(atkCount):
            if miss(user, target) == False:
                target.hp -= atkDmg
                print(f" {target.name} took {atkDmg} damage!")
            else:
                print(f" {target.name} dodged...")
        self.cooldown = self.maxCooldown

class AbyssNova (Skill):
    def __init__(self):
        super().__init__(1, 3, "Abyss Nova")
    
    def skill(self, user, target, party):
        target.atkChange1 += user.mag
        target.magChange1 += user.mag
        target.resChange1 -= user.mag
        print(f'{user.name} used Abyss Nova!')
        print (f' {target.name} gained {user.mag} ATK!')
        print (f' {target.name} gained {user.mag} MAG!')
        print (f' {target.name} lost {min(user.mag,target.res)} RES...')
        self.cooldown = self.maxCooldown

class RekindlingOfDeadAshes (Skill):
    def __init__(self):
        super().__init__(3, 3, "Rekindling of Dead Ashes")
    
    def skill(self, user, target, party):
        preHp = target.hp
        if target.hp == 0:
            target.hp = min(target.hp + (user.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + user.mag, target.maxHp)
        healed = target.hp - preHp
        print(f"{user.name} used Rekindling Of Dead Ashes!")
        print(f" {target.name} recovered {healed} HP!")
        self.cooldown = self.maxCooldown

class Supersonic (Skill):
    def __init__(self):
        super().__init__(2, 3, "Supersonic")
    
    def skill(self, user, target, party):
        target.atkChange1 -= user.atk
        print(f'{user.name} uses Supersonic on {target.name}!')
        print(f' {target.name} lost {min(user.atk, target.atk)} ATK...')
        self.cooldown = self.maxCooldown

class QuickAttack (Skill):
    def __init__(self):
        super().__init__(0, 2, "Quick Attack")
    
    def skill(self, user, target, party):
        user.spd *= 2
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 2 * critMod) - target.dfn),0)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for i in range(atkCount):
            if miss(user, target) == False:
                target.hp -= atkDmg
                print(f" {target.name} took {atkDmg} damage!")
            else:
                print(f" {target.name} dodged...")
        self.cooldown = self.maxCooldown

class Sludge (Skill):
    def __init__(self):
        super().__init__(4, 3, "Sludge")

    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for x in party:
            atkDmg = max(round((user.mag * 2 * critMod) - x.res),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    print(f" {x.name} took {atkDmg} damage!")
                else:
                    print(f" {x.name} dodged...")
        self.cooldown = self.maxCooldown