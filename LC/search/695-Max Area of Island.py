# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/14 8:41 AM


from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # method-1: DFS
        self.m, self.n = len(grid), len(grid[0])
        max_area = 0
        for row in range(self.m):
            for col in range(self.n):
                max_area = max(max_area, self.dfs(grid, row, col))
        return max_area

    def dfs(self, grid, x, y):
        if (x >= self.m) or (x < 0) or (y >= self.n) or (y < 0) or (grid[x][y] == 0):
            return 0
        grid[x][y] = 0
        area = 1
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            area += self.dfs(grid, x + dir[0], y + dir[1])
        return area

if __name__ == '__main__':
    obj = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(obj.maxAreaOfIsland(grid))