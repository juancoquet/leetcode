from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":
                    islands += 1
                    sink_island(grid, x, y)
        return islands


DIRECTIONS = {
    (0, -1),  # north
    (1, 0),  # east
    (0, 1),  # south
    (-1, 0),  # west
}


def sink_island(grid: list[list[str]], x: int, y: int) -> None:
    """Sinks all points (if any) belonging to an island at (x, y)"""
    to_visit = deque([(x, y)])
    grid[y][x] = "0"

    max_x, max_y = len(grid[0]) - 1, len(grid) - 1

    while to_visit:
        x, y = to_visit.popleft()
        for delta_x, delta_y in DIRECTIONS:
            nx, ny = x + delta_x, y + delta_y
            if 0 <= nx <= max_x and 0 <= ny <= max_y and grid[ny][nx] == "1":
                grid[ny][nx] = "0"
                to_visit.append((nx, ny))
