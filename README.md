# lab5
# Repository for labs Laboratory Work: Number of Islands (DFS Implementation)

## Task Description
This laboratory work implements an algorithm to find and count the number of distinct islands in a 2D grid using Depth-First Search (DFS).

## Problem Statement
* A 2D grid is provided where `1` represents land and `0` represents water.
* An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically (diagonal connections do not count).
* The goal is to traverse the grid and determine the total number of isolated islands.
* The grid is allowed to be modified in place to track visited landmasses.

## Objective
Implement the function:
```python
def count_islands(grid: list[list[int]]) -> int:
def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return
        
        grid[r][c] = 0  # Mark as visited
        
        dfs(r - 1, c)   # Up
        dfs(r + 1, c)   # Down
        dfs(r, c - 1)   # Left
        dfs(r, c + 1)   # Right

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                island_count += 1
                dfs(r, c)

    return island_count

if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    print(f"Кількість островів: {count_islands(grid)}")
    Complexity AnalysisTime Complexity: O(M $\times$ N), where M is the number of rows and N is the number of columns. Every cell in the grid is visited and processed exactly once.Space Complexity: O(M $\times$ N) in the worst-case scenario (if the entire grid is a single island), due to the recursion stack of the DFS approach.ExamplesExample 1Input:Pythongrid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
Output:PlaintextКількість островів: 2
Example 2 (Empty Grid)Input:Pythongrid = []
Output:PlaintextКількість островів: 0
Example 3 (All Water)Input:Pythongrid = [
    [0, 0, 0],
    [0, 0, 0]
]
Output:PlaintextКількість островів: 0
Unit TestingTesting is implemented using Python’s unittest module.Pythonimport unittest
from solution import count_islands

class TestCountIslands(unittest.TestCase):
    def test_example_1(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(count_islands(grid), 2)

    def test_empty_grid(self):
        self.assertEqual(count_islands([]), 0)

    def test_all_water(self):
        grid = [[0, 0], [0, 0]]
        self.assertEqual(count_islands(grid), 0)

    def test_all_land(self):
        grid = [[1, 1], [1, 1]]
        self.assertEqual(count_islands(grid), 1)

    def test_diagonal_islands(self):
        grid = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        self.assertEqual(count_islands(grid), 3)

if __name__ == "__main__":
    unittest.main()
