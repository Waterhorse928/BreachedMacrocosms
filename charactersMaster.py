import math
import random

class Character:
    def __init__(self, level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name):
        self.level = level
        self.exp = exp
        self.hp = (vit * 3) + 40
        self.maxHp = (vit * 3) + 40
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
        self.resBase = res
        self.vitChange = 0
        self.atkChange = 0
        self.magChange = 0
        self.sklChange = 0
        self.spdChange = 0
        self.lukChange = 0
        self.dfnChange = 0
        self.resChange = 0
        self.vitChange1 = 0
        self.atkChange1 = 0
        self.magChange1 = 0
        self.sklChange1 = 0
        self.spdChange1 = 0
        self.lukChange1 = 0
        self.dfnChange1 = 0
        self.resChange1 = 0
        self.skillList = []

    def statUpdate(self):
        preMaxHp = self.maxHp
        self.vit = max(self.vitBase + self.vitChange + self.vitChange1,0)
        self.atk = max(self.atkBase + self.atkChange + self.atkChange1,0)
        self.mag = max(self.magBase + self.magChange + self.magChange1,0)
        self.skl = max(self.sklBase + self.sklChange + self.sklChange1,0)
        self.spd = max(self.spdBase + self.spdChange + self.spdChange1,0)
        self.luk = max(self.lukBase + self.lukChange + self.lukChange1,0)
        self.dfn = max(self.dfnBase + self.dfnChange + self.dfnChange1,0)
        self.res = max(self.resBase + self.resChange + self.resChange1,0)
        self.maxHp = (self.vit * 3) + 40
        if self.hp <= 0:
            self.isAlive = False
            self.hp = 0
        else:
            self.isAlive = True
            hpChange = self.maxHp - preMaxHp
            self.hp = max(self.hp + hpChange,1)

    def rotateStatChanges(self):
        self.vitChange = self.vitChange1
        self.atkChange = self.atkChange1
        self.magChange = self.magChange1
        self.sklChange = self.sklChange1
        self.spdChange = self.spdChange1
        self.lukChange = self.lukChange1
        self.dfnChange = self.dfnChange1
        self.resChange = self.resChange1
        self.vitChange1 = 0
        self.atkChange1 = 0
        self.magChange1 = 0
        self.sklChange1 = 0
        self.spdChange1 = 0
        self.lukChange1 = 0
        self.dfnChange1 = 0
        self.resChange1 = 0
        self.statUpdate()
        
    def removeStatChanges(self): # unused
        self.vitChange -= 0
        self.atkChange -= 0
        self.magChange -= 0
        self.sklChange -= 0
        self.spdChange -= 0
        self.lukChange -= 0
        self.dfnChange -= 0
        self.resChange -= 0

    def lowerStatChanges(self): # unused
        self.vitChange = self.vitChange * (1 - 0.25)
        self.atkChange = self.atkChange * (1 - 0.25)
        self.magChange = self.magChange * (1 - 0.25)
        self.sklChange = self.sklChange * (1 - 0.25)
        self.spdChange = self.spdChange * (1 - 0.25)
        self.lukChange = self.lukChange * (1 - 0.25)
        self.dfnChange = self.dfnChange * (1 - 0.25)
        self.resChange = self.resChange * (1 - 0.25)

        if self.vitChange >= 0:
            self.vitChange = math.floor(self.vitChange)
        else:
            self.vitChange = math.ceil (self.vitChange)

        if self.atkChange >= 0:
            self.atkChange = math.floor(self.atkChange)
        else:
            self.atkChange = math.ceil (self.atkChange)

        if self.magChange >= 0:
            self.magChange = math.floor(self.magChange)
        else:
            self.magChange = math.ceil (self.magChange)

        if self.sklChange >= 0:
            self.sklChange = math.floor(self.sklChange)
        else:
            self.sklChange = math.ceil (self.sklChange)

        if self.spdChange >= 0:
            self.spdChange = math.floor(self.spdChange)
        else:
            self.spdChange = math.ceil (self.spdChange)

        if self.lukChange >= 0:
            self.lukChange = math.floor(self.lukChange)
        else:
            self.lukChange = math.ceil (self.lukChange)

        if self.dfnChange >= 0:
            self.dfnChange = math.floor(self.dfnChange)
        else:
            self.dfnChange = math.ceil (self.dfnChange)

        if self.resChange >= 0:
            self.resChange = math.floor(self.resChange)
        else:
            self.resChange = math.ceil (self.resChange)
        self.statUpdate
        # was there an easier way to this? Probably.
            

 