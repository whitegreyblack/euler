# problem 15
# Lattice paths
"""
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

+---+---+
|   |   |
+---+---+
|   |   |
+---+---O

+---+---+
        |
        +
        |
        O

+---+
    |
    +---+
        |
        O

+---+
    |
    +
    |
    +---O

+
|
+---+---+
        |
        O

+
|
+---+
    |
    +---O

+
|
+
|
+---+---O

How many such routes are there through a 20×20 grid?
"""

# solution
"""
Imagine the grid as a graph

                NW
               /  \
              WW  NN
             /  \/  \
           SW   CC   NE
             \  /\  /
              SS  EE
               \  /
                SE 

                NW
                /\
               W  N
             / |  | \
           SW  C  C  NE
          /  / |  | \  \
         S  S  E  S  E  E
         |  |  |  |  |  |
         SE SE SE SE SE SE
"""
size = 20
grid = [[1 if i == size or j == size else 0 
          for i in range(size+1)] 
            for j in range(size+1)]

for j in range(size-1, -1, -1):
    for i in range(size-1, -1, -1):
        grid[j][i] = grid[j+1][i] + grid[j][i+1]

for j in grid:
  print(j)

import operator as op
import functools as fn
print(fn.reduce(op.mul, range(1, 22), 1))
print(fn.reduce(op.mul, range(1, 22), 1)//20)
print(list(range(1, 22)))