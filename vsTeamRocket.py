import math
import random
import charactersPlayer
import charactersEnemy

print(f"{charactersPlayer.tyCharacters[0]}:")
print(f" 1. {charactersPlayer.tyCharacters[1].name}")
print(f" 2. {charactersPlayer.tyCharacters[2].name}")

player = {}

for x in range(1, min(len(charactersPlayer.tyCharacters), 5)):
    player[int(x)] = input(f"Choose a character for slot {x}: ")
    player[int(x)] = int(player[int(x)])
    player[int(x)] = charactersPlayer.tyCharacters[player[int(x)]]

print(f"{player[1].name}'s Skills:")
for x in range(len(player[1].skillList)):
    print(f" {x}. {player[1].skillList[x].name}")



player[1].skillList[1].skill(player[1],player[2])



act1 = input("Use which number skill?: ")



