# Conway's Game Of Life

The "game" is actually a zero-player game, meaning that its evolution is
determined by its initial state, needing no input from human players. One
interacts with the Game of Life by creating an initial configuration and
observing how it evolves. The rules for cells are as follows:

- Any live cell with fewer than two live neighbours dies, as if caused by under-population.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overcrowding.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The game continuously plays out running each iteration through this ruleset.
