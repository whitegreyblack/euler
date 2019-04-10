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

import operator as op
import functools as fn
import click


def bottom_edge(size, x, y) -> int:
    return int(x == size or y == size)

def build_grid(size:int) -> list:
    return [[bottom_edge(size, i, j) for i in range(size+1)] for j in range(size+1)]

def populate_grid(grid:list) -> None:
    size = len(grid) - 1
    for j in range(size-1, -1, -1):
        for i in range(size-1, -1, -1):
            try:
                grid[j][i] = grid[j+1][i] + grid[j][i+1]
            except:
                print(i, j)
                raise

def count_paths(grid:list) -> int:
    return grid[0][0]

def print_grid(grid:list) -> None:
    for g in grid:
        print(g)

@click.command()
@click.argument('size', nargs=1)
def main(size):
    grid = build_grid(int(size))
    populate_grid(grid)
    print_grid(grid)
    print(count_paths(grid))

if __name__ == "__main__":
    main()
