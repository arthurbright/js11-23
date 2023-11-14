A simulator for the Nov 2023 Jane Street puzzle.

# Usage
Run `python sim.py` to run the simulation.

To change the starting grid/inputs, change the imported module name on line 1.

A valid starting setup module must provide `grid`, `SIZE`, and `INPUT`.

See `grid8.py` and `grid4.py` for examples.

After going through the provided `INPUT`, the program will ask for input.

When the state of the grid is printed, red represents your current position, and green represents tiles that will sink if you stay still. Also, the value of n is printed for convenience.