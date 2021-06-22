import random
import charactersMaster

class Rattata(charactersMaster.Character):
    def quickAttack(self, target):
        print('Rattata uses Quick Attack!')

class Zubat(charactersMaster.Character):
    def supersonic(self, target):
        target.atkChange -= self.atk
        print(f'Zubat uses Supersonic on {target.name}!')
        print(f'{target.name} lost {min(self.atk, target.atk)} ATK...')

class Muk(charactersMaster.Character):
    def sludge(self, target):
        print('Muk uses Sludge!')