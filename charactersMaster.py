import random

def multipleAttack(attacker, defender):
    attackCount = 1
    if attacker.spd > defender.spd:
        multipleAttackChance = attacker.spd - defender.spd
        while multipleAttackChance > 1:
            multipleAttackCheck = random.randint(1, 100)
            if multipleAttackChance >= multipleAttackCheck:
                attackCount += 1
            else:
                break
            multipleAttackChance /= 2
    return attackCount
print('Multiple attacks is working!')

def crit(attacker, defender):
    critMultiplier = 1
    if attacker.skl > defender.luk:
        critChance = attacker.skl - defender.luk
        while critChance > 1:
            critCheck = random.randint(1, 100)
            if critChance >= critCheck:
                critMultiplier += 0.5
            else:
                break
            critChance /= 2
    return critMultiplier
print('Crits are working!')

def miss(attacker, defender):
    miss = False
    if attacker.skl < defender.luk:
        missChance = (defender.luk * 2) - (attacker.skl * 2)
        missCheck = random.randint(1, 100)
        if missChance >= missCheck:
            miss = True
    return miss
print('Misses are working!')

class Character:
    def __init__(self, level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name):
        self.level = level
        self.exp = exp
        self.hp = (vit * 2) + 20
        self.maxHp = (vit * 2) + 20
        self.vit = vit
        self.atk = atk
        self.mag = mag
        self.skl = skl
        self.spd = spd
        self.luk = luk
        self.dfn = dfn
        self.res = res
        self.isAlive = True
        self.isEnemy = isEnemy
        self.name = name
        self.turnNumber = 0
        self.vitBase = vit
        self.atkBase = atk
        self.magBase = mag
        self.sklBase = skl
        self.spdBase = spd
        self.lukBase = luk
        self.dfnBase = dfn
        self.resBase = 0
        self.vitChange = 0
        self.atkChange = 0
        self.magChange = 0
        self.sklChange = 0
        self.spdChange = 0
        self.lukChange = 0
        self.dfnChange = 0
        self.resChange = 0
        
    def basicAttack(self, defender):
        atkDmg = (self.atk * 2 * crit(self, defender)) - defender.dfn
        if atkDmg > 0:
            for i in range(multipleAttack(self, defender)):
                if defender.hp > 0:
                    if miss(self, defender) == False:
                        defender.hp -= atkDmg
                else:
#                    defender.ko()
                    break
   
    def statUpdate(self):
        preMaxHp = self.maxHp
        self.vit = max(self.vitBase + self.vitChange,0)
        self.atk = max(self.atkBase + self.atkChange,0)
        self.mag = max(self.magBase + self.magChange,0)
        self.skl = max(self.sklBase + self.sklChange,0)
        self.spd = max(self.spdBase + self.spdChange,0)
        self.luk = max(self.lukBase + self.lukChange,0)
        self.dfn = max(self.dfnBase + self.dfnChange,0)
        self.res = max(self.resBase + self.resChange,0)
        self.maxHp = (self.vit * 2) + 20
        hpChange = self.maxHp - preMaxHp
        self.hp = max(self.hp + hpChange,1)
        print('Stat Update run.')
    print('Stat Update entered.')
