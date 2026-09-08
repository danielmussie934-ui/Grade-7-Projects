import pygame
import numpy as np
import random
player_grid = np.zeros((20, 20), dtype=int)
cpu_grid = np.zeros((20, 20), dtype=int)
cpu_score = 0
player_score = 0
def getships():
  try:
   battleship = input("Where do you want to place your battleship? (row, column): ").split(" ")
   battleship = [int(x) for x in battleship]
   player_grid[battleship[0]][battleship[1]] = 1
   player_grid[battleship[0]][battleship[1]+1] = 1
   player_grid[battleship[0]][battleship[1]+2] = 1
   cpu_battleship =  [random.randint(0, 20), random.randint(0, 20)]
   # Set up cpu battleship on the grid  
   cpu_grid[cpu_batttleship[0]][cpu_batttleship[1]] = 1
   cpu_grid[cpu_batttleship[0]][cpu_batttleship[1]+1] = 1
   cpu_grid[cpu_batttleship[0]][cpu_batttleship[1]+2] = 1
   main()
  except ValueError:
    print("Invalid input. Please enter integers.\n")
    getships()
def checkships(row, column):

  global cpu_score, player_score
  if player_grid[row][column] == 1:
     player_grid[row][column] = 0
     cpu_score += 1
     return "C"
  elif cpu_grid[row][column] == 1:
    cpu_grid[row][column] = 0
    player_score += 1
    return "P"
def check_winner():
    if np.sum(player_grid) == 0:
        print("CPU wins!")
        return "CPU"
    elif np.sum(cpu_grid) == 0:
        print("Player wins!")
        return "Player"
    else:
        return None

def main():
    row = int(input("Enter row to attack (0-19): "))
    column = int(input("Enter column to attack (0-19): "))
    result = checkships(row, column)
    if result == "C":
        print("Your ship was hit!")
    elif result == "P":
        print("You hit the CPU's ship!")
    is_winner = check_winner()
    if is_winner:
        print(f"{is_winner} wins the game!")
        return
    else:
        main()





getships()

