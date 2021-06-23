import random
import charactersMaster

class Rattata(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 15, 20, 0, 10, 20, 10, 15, 15, True, "Rattata")
        self.atkName = "Tackle"
    def quickAttack(self, target):
        print('Rattata uses Quick Attack!')

class Zubat(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 10, 10, 10, 15, 15, 25, 10, 10, True, 'Zubat')
        self.atkName = "Bite"
    def supersonic(self, target):
        target.atkChange -= self.atk
        print(f'Zubat uses Supersonic on {target.name}!')
        print(f'{target.name} lost {min(self.atk, target.atk)} ATK...')

class Muk(charactersMaster.Character):
    def __init__(self):
        super().__init__(1, 0, 20, 10, 15, 10, 5, 5, 20, 20, True, 'Muk')
        self.atkName = "Pound"
    def sludge(self, target):
        print('Muk uses Sludge!')