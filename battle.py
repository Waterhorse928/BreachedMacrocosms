import math
import random
import charactersPlayer
import charactersEnemy

utsuho = charactersPlayer.Utsuho(1, 0, 27, 5, 32, 12, 2, 4, 28, 26, False, "Utsuho")
orin = charactersPlayer.Orin(1, 0, 16, 17, 22, 19, 32, 29, 10, 15, False, "Orin")
rattata = charactersEnemy.Rattata(1, 0, 15, 20, 0, 10, 20, 10, 15, 15, True, "Rattata")
zubat = charactersEnemy.Zubat(1, 0, 10, 10, 10, 15, 15, 25, 10, 10, True, 'Zubat')
muk = charactersEnemy.Muk(1, 0, 20, 10, 15, 10, 5, 5, 20, 20, True, 'Muk')

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


print(f"Utsuho's HP is {utsuho.hp}")
utsuho.hp = 0
print(f"Utsuho's HP is {utsuho.hp}")
orin.rekindlingOfDeadAshes(utsuho)
print(f"Utsuho's HP is {utsuho.hp}")
orin.rekindlingOfDeadAshes(utsuho)
print(f"Utsuho's HP is {utsuho.hp}")
orin.rekindlingOfDeadAshes(utsuho)
print(f"Utsuho's HP is {utsuho.hp}")

print(f"Utsuho's ATK is {utsuho.atk}")
print(f"Utsuho's MAG is {utsuho.mag}")
print(f"Utsuho's RES is {utsuho.res}")
utsuho.abyssNova(utsuho)
utsuho.statUpdate()
print(f"Utsuho's ATK is {utsuho.atk}")
print(f"Utsuho's MAG is {utsuho.mag}")
print(f"Utsuho's RES is {utsuho.res}")

utsuho.atkChange = 0
utsuho.statUpdate()
print(f"Utsuho's ATK is {utsuho.atk}")
print(f"Zubat's ATK is {zubat.atk}")
zubat.supersonic(utsuho)
utsuho.statUpdate()
print(f"Utsuho's ATK is {utsuho.atk}")
print(f"Zubat's ATK is {zubat.atk}")