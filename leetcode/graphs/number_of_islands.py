from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited: set[tuple[int, int]] = set()  # {(x, y), ...}
        islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if (x, y) in visited:
                    continue
                if cell == "1":
                    islands += 1
                    island_points = bfs(grid, x, y)
                    visited |= island_points
        return islands


DIRECTIONS = {
    (0, -1),  # north
    (1, 0),  # east
    (0, 1),  # south
    (-1, 0),  # west
}


def bfs(grid: list[list[str]], x: int, y: int) -> set[tuple[int, int]]:
    """Returns all points (if any) belonging to an island at (x, y)"""
    island_points: set[tuple[int, int]] = set()
    visited: set[tuple[int, int]] = set()
    to_visit: list[tuple[int, int]] = [(x, y)]

    while to_visit:
        curr = to_visit.pop(0)
        visited.add(curr)
        x, y = curr
        if is_land(grid, x, y):
            island_points.add((x, y))
            new_points = {(x + delta_x, y + delta_y) for delta_x, delta_y in DIRECTIONS} - visited
            to_visit.extend(new_points)

    return island_points


def is_land(grid: list[list[str]], x: int, y: int) -> bool:
    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1
    if not 0 <= y <= max_y:
        return False
    if not 0 <= x <= max_x:
        return False
    return grid[y][x] == "1"
