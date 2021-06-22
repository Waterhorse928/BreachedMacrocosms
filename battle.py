import math
import random
import charactersPlayer
import charactersEnemy

utsuho = charactersPlayer.Utsuho(1, 0, 27, 29, 32, 12, 2, 4, 28, 26, False, "Utsuho")
rattata = charactersEnemy.Rattata(1, 0, 15, 20, 0, 10, 20, 10, 15, 15, True, "Rattata")

def turnOrder(self):
    return self.turnNumber

aliveCharacters = []
deadCharacters = []

aliveCharacters.append(utsuho)
aliveCharacters.append(rattata)
print(aliveCharacters[0].name)
print(aliveCharacters[1].name)

for x in aliveCharacters:
    print(x)
    x.turnNumber = x.spd + random.randint(0, 5)

aliveCharacters.sort(key = turnOrder, reverse = True)
print(aliveCharacters[0].name)
print(aliveCharacters[1].name)

print(utsuho.atk)
print(utsuho.atkChange)

utsuho.atkChange = -30
utsuho.statUpdate()

print(utsuho.atk)
print(utsuho.atkChange)