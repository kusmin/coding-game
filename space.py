import math
import sys

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    dic_mountain = {}
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        dic_mountain[i] = mountain_h
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on
    print(dic_mountain)
    index = 0
    maior_valor = 0
    for k, v in dic_mountain.items():
      print(k, v)
      print("maior valor antes:", maior_valor)
      if v > maior_valor:
        index = k
        print("marior valor depois: ",maior_valor)

    print("index: ", index)     
