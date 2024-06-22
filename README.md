# Roller Coaster Path Finder
An amusement park wants to build the tallest roller coaster possible by making the best use of the surrounding terrain. Given a 2D representation of the terrain, this project determines the longest possible slope—the longest downward path that could be used for the roller coaster’s main drop.

## Problem Description
The terrain is represented by a topographical map, which is a two-dimensional grid of elevations. Each grid cell contains an integer height elevation. The task is to find the longest sequence of grid locations from a high elevation to a low elevation. The path must always move downhill and can only travel to adjacent cells (up, down, left, right), but not diagonally.

## Installation and Use
1. Clone the repository:
   ```sh
   git clone https://github.com/mo-austin/roller-coaster.git
   cd roller-coaster
2. Run the main script:
   ```sh
   python main.py

## Input
The input file terrain.txt contains:

1. The number of rows m.
2. The number of columns n.
3. The 2D grid of integers representing elevations.

## Output
The program outputs:

1. The length of the longest downhill slope.
2. The ordered terrain values in the slope from highest to lowest elevation.
3. The starting position for the coaster’s drop.

## Solution
Top-down DP with memoization
1. Divide: Identify possible paths from each cell
2. Conquer: Use DP to recursively compute the longest path from each cell.
3. Combine: Merge the results to find the overall longest downhill path.


