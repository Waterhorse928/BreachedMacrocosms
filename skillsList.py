import random

# Skill Types
# 0 = One Target Attack
# 1 = One Target Buff
# 2 = One Target Debuff
# 3 = One Target Heal
# 4 = Party Attack
# 5 = Party Buff
# 6 = Party Debuff
# 7 = Party Heal

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
        self.maxCooldown = cooldown+1
        self.name = name

class BasicAttack (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class AbyssNova (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.atkChange1 += user.mag
        target.magChange1 += user.mag
        target.resChange1 -= user.mag
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.mag} ATK!')
        print (f' {target.name} gained {user.mag} MAG!')
        print (f' {target.name} lost {min(user.mag,target.res)} RES...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class RekindlingOfDeadAshes (Skill):
    def __init__(self, cooldown, name):
        super().__init__(3, cooldown, name)
    
    def skill(self, user, target, party):
        preHp = target.hp
        if target.hp == 0:
            target.hp = min(target.hp + (user.mag * 2), target.maxHp)
        else:
            target.hp = min(target.hp + user.mag, target.maxHp)
        healed = target.hp - preHp
        print(f"{user.name} used {self.name}")
        print(f" {target.name} recovered {healed} HP!")
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Supersonic (Skill):
    def __init__(self, cooldown, name):
        super().__init__(2, cooldown, name)
    
    def skill(self, user, target, party):
        target.atkChange1 -= user.atk
        print(f'{user.name} uses {self.name}')
        print(f' {target.name} lost {min(user.atk, target.atk)} ATK...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class QuickAttack (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Sludge (Skill):
    def __init__(self, cooldown, name):
        super().__init__(4, cooldown, name)

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
            if x.hp <= 0:
                print(f" {x.name} was knocked out!")
            x.statUpdate()
        self.cooldown = self.maxCooldown

class GeyserColumn (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.mag * 3 * critMod) - target.res),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Curse (Skill):
    def __init__(self, cooldown, name):
        super().__init__(2, cooldown, name)

    def skill(self, user, target, party):
        target.lukChange1 -= user.mag
        print(f'{user.name} uses {self.name}!')
        print(f' {target.name} lost {min(user.mag, target.luk)} LUK...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Heal (Skill):
    def __init__(self, cooldown, name):
        super().__init__(3, cooldown, name)

    def skill(self, user, target, party):
        preHp = target.hp
        target.hp = min(target.hp + user.mag, target.maxHp)
        healed = target.hp - preHp
        print(f"{user.name} used {self.name}!")
        print(f" {target.name} recovered {healed} HP!")
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Maul (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 3 * critMod) - target.dfn),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class OpticalCamouflage (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.lukChange1 += user.skl
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.skl} LUK!')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class MagicMissile (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.mag * 2 * critMod) - (target.res * 0.5)),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Shoot (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        user.skl *= 2
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class WatchOut (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.lukChange1 += user.atk
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.atk} LUK!')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Savage (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 4 * critMod) - target.dfn),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Miracle (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.lukChange1 += user.mag
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.mag} LUK!')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Thinking (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.sklChange1 += user.skl
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.skl} SKL!')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Howl (Skill):
    def __init__(self, cooldown, name):
        super().__init__(2, cooldown, name)
    
    def skill(self, user, target, party):
        target.dfnChange1 -= user.atk
        print(f'{user.name} used {self.name}!')
        print(f' {target.name} lost {min(user.atk, target.dfn)} DEF...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Heat (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        power = round (user.atk * 0.5)
        target.atkChange1 += user.atk
        target.sklChange1 += user.atk
        target.vitChange1 -= power
        target.magChange1 -= power
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.atk} ATK!')
        print (f' {target.name} gained {user.atk} SKL!')
        print (f' {target.name} lost {min(power,target.vit)} VIT...')
        print (f' {target.name} lost {min(power,target.mag)} MAG...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Sun (Skill):
    def __init__(self, cooldown, name):
        super().__init__(4, cooldown, name)

    def skill(self, user, target, party):
        target.luk *= 0.5
        critMod = crit(user, target)
        target.luk *= 2
        atkCount = multipleAttack(user, target)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for x in party:
            x.luk *= 0.5
            atkDmg = max(round((user.mag * 3 * critMod) - x.res),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    print(f" {x.name} took {atkDmg} damage!")
                else:
                    print(f" {x.name} dodged...")
            if x.hp <= 0:
                print(f" {x.name} was knocked out!")
            x.statUpdate()
        self.cooldown = self.maxCooldown

class BlazingDragon (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        user.skl *= 2
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 3 * critMod) - target.dfn),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class CatsWalk (Skill):
    def __init__(self, cooldown, name):
        super().__init__(4, cooldown, name)

    def skill(self, user, target, party):
        user.spd *= 2
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for x in party:
            atkDmg = max(round((user.atk * 2 * critMod) - x.dfn),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    print(f" {x.name} took {atkDmg} damage!")
                else:
                    print(f" {x.name} dodged...")
            if x.hp <= 0:
                print(f" {x.name} was knocked out!")
            x.statUpdate()
        self.cooldown = self.maxCooldown

class Smokescreen (Skill):
    def __init__(self, cooldown, name):
        super().__init__(6, cooldown, name)

    def skill(self, user, target, party):
        print(f'{user.name} used {self.name}!')
        for x in party:
            power = round (user.mag * 0.5)
            x.sklChange1 -= power
            print (f' {x.name} lost {min(power,x.skl)} SKL...')
            x.statUpdate()
        self.cooldown = self.maxCooldown

class Smog (Skill):
    def __init__(self, cooldown, name):
        super().__init__(4, cooldown, name)

    def skill(self, user, target, party):
        user.skl *= 0.5
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for x in party:
            atkDmg = max(round((user.mag * 3 * critMod) - x.res),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    print(f" {x.name} took {atkDmg} damage!")
                else:
                    print(f" {x.name} dodged...")
            if x.hp <= 0:
                print(f" {x.name} was knocked out!")
            x.statUpdate()
        self.cooldown = self.maxCooldown

class Wrap (Skill):
    def __init__(self, cooldown, name):
        super().__init__(2, cooldown, name)

    def skill(self, user, target, party):
        target.spdChange1 -= user.atk
        print(f'{user.name} uses {self.name}!')
        print(f' {target.name} lost {min(user.atk, target.spd)} SPD...')
        self.cooldown = self.maxCooldown

class Acid (Skill):
    def __init__(self, cooldown, name):
        super().__init__(6, cooldown, name)

    def skill(self, user, target, party):
        print(f'{user.name} used {self.name}!')
        for x in party:
            x.dfnChange1 -= user.atk
            print (f' {x.name} lost {min(user.atk,x.dfn)} DEF...')
            x.statUpdate()
        self.cooldown = self.maxCooldown

class PoisonSting (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        target.dfn = round(target.dfn * 0.5)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class FurySwipes (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        user.atk *= 0.5
        user.spd *= 4
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class DarkStar (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.sklChange1 += user.atk
        target.spdChange1 += user.atk
        target.dfnChange1 -= user.atk
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.atk} SKL!')
        print (f' {target.name} gained {user.atk} SPD!')
        print (f' {target.name} lost {min(user.atk,target.dfn)} DEF...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class ShadowTag (Skill):
    def __init__(self, cooldown, name):
        super().__init__(6, cooldown, name)

    def skill(self, user, target, party):
        print(f'{user.name} used {self.name}!')
        for x in party:
            power = round(user.vit * 0.3)
            x.spdChange1 -= power
            x.lukChange1 -= power
            print (f' {x.name} lost {min(power,x.spd)} SPD...')
            print (f' {x.name} lost {min(power,x.luk)} LUK...')
            x.statUpdate()
        self.cooldown = self.maxCooldown

class Bide (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        power = round(user.vit * 0.5)
        target.dfnChange1 += power
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {power} DEF!')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Counter (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        power = round(user.vit * 0.2)
        target.dfnChange1 += power
        target.atkChange1 += power
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {power} DEF!')
        print (f' {target.name} gained {power} ATK!')
        self.cooldown = self.maxCooldown

class MirrorCoat (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        power = round(user.vit * 0.2)
        target.resChange1 += power
        target.magChange1 += power
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {power} RES!')
        print (f' {target.name} gained {power} MAG!')
        self.cooldown = self.maxCooldown

class ShadowClaw (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        user.skl *= 3
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class SnuggleForever (Skill):
    def __init__(self, cooldown, name):
        super().__init__(4, cooldown, name)

    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for x in party:
            atkDmg = max(round((user.atk * 4 * critMod) - x.dfn),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    print(f" {x.name} took {atkDmg} damage!")
                else:
                    print(f" {x.name} dodged...")
            if x.hp <= 0:
                print(f" {x.name} was knocked out!")
            x.statUpdate()
        self.cooldown = self.maxCooldown

class SleepPowder (Skill):
    def __init__(self, cooldown, name):
        super().__init__(2, cooldown, name)

    def skill(self, user, target, party):
        power = round (user.atk)
        target.lukChange1 -= power
        target.sklChange1 -= power
        print(f'{user.name} uses {self.name}!')
        print(f' {target.name} lost {min(power, target.luk)} LUK...')
        print(f' {target.name} lost {min(power, target.skl)} SKL...')
        self.cooldown = self.maxCooldown

class SwordsDance (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        power = round (user.atk * 2)
        target.atkChange1 += power
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {power} ATK!')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class NightShade (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.mag * 2 * critMod) - (target.res * 0)),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Wisp (Skill):
    def __init__(self, cooldown, name):
        super().__init__(2, cooldown, name)
    
    def skill(self, user, target, party):
        target.atkChange1 -= user.mag
        print(f'{user.name} uses {self.name}')
        print(f' {target.name} lost {min(user.atk, target.mag)} ATK...')
        self.cooldown = self.maxCooldown
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class ShowMeRock (Skill):
    def __init__(self, cooldown, name):
        super().__init__(1, cooldown, name)
    
    def skill(self, user, target, party):
        target.atkChange1 += user.vit
        print(f'{user.name} used {self.name}!')
        print (f' {target.name} gained {user.vit} ATK!')
        self.cooldown = self.maxCooldown

class Repair (Skill):
    def __init__(self, cooldown, name):
        super().__init__(3, cooldown, name)

    def skill(self, user, target, party):
        preHp = target.hp
        target.hp = min(target.hp + user.skl, target.maxHp)
        healed = target.hp - preHp
        print(f"{user.name} used {self.name}!")
        print(f" {target.name} recovered {healed} HP!")
        target.atkChange1 += user.skl
        print (f' {target.name} gained {user.skl} ATK!')
        self.cooldown = self.maxCooldown

class PhotonTorpedo (Skill):
    def __init__(self, cooldown, name):
        super().__init__(0, cooldown, name)
    
    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        atkDmg = max(round((user.atk * 3 * critMod) - target.res),0)
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
        if target.hp <= 0:
            print(f" {target.name} was knocked out!")

class Cleave (Skill):
    def __init__(self, cooldown, name):
        super().__init__(4, cooldown, name)

    def skill(self, user, target, party):
        critMod = crit(user, target)
        atkCount = multipleAttack(user, target)
        print(f"{user.name} used {self.name}!")
        if critMod != 1:
            print(f" x{critMod} Critical!")
        if atkCount != 1:
            print(f" {user.name} attacked {atkCount} times!")
        for x in party:
            atkDmg = max(round((user.atk * 2 * critMod) - x.dfn),0)
            for i in range(atkCount):
                if miss(user, x) == False:
                    x.hp -= atkDmg
                    print(f" {x.name} took {atkDmg} damage!")
                else:
                    print(f" {x.name} dodged...")
            if x.hp <= 0:
                print(f" {x.name} was knocked out!")
            x.statUpdate()
        self.cooldown = self.maxCooldown
