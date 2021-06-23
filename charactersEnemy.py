import random
import charactersMaster

class Rattata(charactersMaster.Character):
    def __init__(self, level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name):
        super().__init__(level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name)
        self.atkName = "Tackle"
    def quickAttack(self, target):
        print('Rattata uses Quick Attack!')

class Zubat(charactersMaster.Character):
    def __init__(self, level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name):
        super().__init__(level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name)
        self.atkName = "Bite"
    def supersonic(self, target):
        target.atkChange -= self.atk
        print(f'Zubat uses Supersonic on {target.name}!')
        print(f'{target.name} lost {min(self.atk, target.atk)} ATK...')

class Muk(charactersMaster.Character):
    def __init__(self, level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name):
        super().__init__(level, exp, vit, atk, mag, skl, spd, luk, dfn, res, isEnemy, name)
        self.atkName = "Pound"
    def sludge(self, target):
        print('Muk uses Sludge!')