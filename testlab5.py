import unittest
import copy

def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0
    
    grid_copy = copy.deepcopy(grid)

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid_copy[r][c] == 0:
            return
        
        grid_copy[r][c] = 0
        
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        dfs(r - 1, c - 1)
        dfs(r - 1, c + 1)
        dfs(r + 1, c - 1)
        dfs(r + 1, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == 1:
                island_count += 1
                dfs(r, c)

    return island_count

class TestCountIslands(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual(count_islands([]), 0)

    def test_all_water(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(count_islands(grid), 0)

    def test_all_land(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(count_islands(grid), 1)

    def test_diagonal_connection(self):
        grid = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        self.assertEqual(count_islands(grid), 1)

    def test_single_cells(self):
        grid = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        self.assertEqual(count_islands(grid), 4)

    def grid(self):
        grid = [
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0]
        ]
        self.assertEqual(count_islands(grid), 5)


if __name__ == '__main__':
    unittest.main()