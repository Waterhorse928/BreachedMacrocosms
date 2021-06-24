import random

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
        self.skillList = []
        
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
        if self.hp <= 0:
            self.isAlive = False
            self.hp = 0
        else:
            hpChange = self.maxHp - preMaxHp
            self.hp = max(self.hp + hpChange,1)



 