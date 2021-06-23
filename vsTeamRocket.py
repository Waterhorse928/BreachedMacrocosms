import math
import random
import charactersPlayer
import charactersEnemy

print("Ty's Characters:")
print(f" 0. {charactersPlayer.tyCharacters[0].name}")
print(f" 1. {charactersPlayer.tyCharacters[1].name}")

player1 = input("Choose a character for slot 1: ")
player1 = int(player1)
player1 = charactersPlayer.tyCharacters[player1]

print(f"{player1.name}'s Skills:")
for x in range(len(player1.skillList)):
    print(f" {x}. {player1.skillList[x][0]}")