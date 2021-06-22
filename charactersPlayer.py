import random
import charactersMaster

class Utsuho(charactersMaster.Character):
    basicAttackName = 'Control Rod Crush'
    def abyssNova(self, target):
        target.atkChange += self.mag
        target.magChange += self.mag
        target.resChange -= self.mag
        print('abyssNova function run')
    

