# cellular-automata

## About cellular-automata

cellular-automata is a simple, interactive simulation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) built using [`pygame`](https://www.pygame.org/docs/) in Python. It is a graphical-user interface based project.

*Date of creation:* `31 May, 2021`

This project is a [zero-player game](https://en.wikipedia.org/wiki/Zero-player_game). The game can be played on a variable-sized (finite) grid. An initial configuration (called <b>seed</b>) of cells is marked *<b>live/active</b>* on the grid. The simulation is started and it is observed how it evolves in the future generations by interactions with the past generations. The Game of Life is a simple model of simple populations.

An interesting list of seeds can be found <b>[here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns)</b>.

## The Rules

The universe of this game is a finite 2-dimensional grid of cells, each of which is either *<b>alive</b>* or *<b>dead</b>*. In between every generation, every cell interacts with its eight [moore-neighbours](https://en.wikipedia.org/wiki/Moore_neighborhood), and the following transitions occur:
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with exactly two or three live neighbours surrvives.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes alive, as if by reproduction

## Footnotes

The real Game of Life takes place on an [infinite two-dimensional orthogonal grid of squares](https://en.wikipedia.org/wiki/Square_tiling). However, the project deals with a variable, yet finite size of grid. The cells at the boundary are treated as though they have less neighbours.

## Run

To play, clone the repository on your device, navigate to the folder, and execute:

```
python3 main.py
```

## Future Plans

- Implementation of periodic boundary (torus) conditions in place of hard boundary (rectangular) conditions

## References

- [Cellular Automaton](https://en.wikipedia.org/wiki/Cellular_automaton)
- [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [The Physics of Self-Replication and Nano-Technology (YouTube)](https://www.youtube.com/watch?v=0wAYZcqSS60)
- [Up and Atom (YouTube)](https://www.youtube.com/c/UpandAtom)
