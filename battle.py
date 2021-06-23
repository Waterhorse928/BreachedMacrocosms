import math
import random
import charactersPlayer
import charactersEnemy

utsuho = charactersPlayer.Utsuho()
orin = charactersPlayer.Orin()
rattata = charactersEnemy.Rattata()
zubat = charactersEnemy.Zubat()
muk = charactersEnemy.Muk()

def turnOrder(self):
    return self.turnNumber

aliveCharacters = []
deadCharacters = []

aliveCharacters.append(utsuho)
aliveCharacters.append(orin)
aliveCharacters.append(rattata)
aliveCharacters.append(zubat)
aliveCharacters.append(muk)
print(aliveCharacters[0].name)
print(aliveCharacters[1].name)

for x in aliveCharacters:
    print(x)
    x.turnNumber = x.spd + random.randint(0, 5)

aliveCharacters.sort(key = turnOrder, reverse = True)
print(aliveCharacters[0].name)
print(aliveCharacters[1].name)


