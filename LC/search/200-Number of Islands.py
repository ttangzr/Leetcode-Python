# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/15 9:28 AM

from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(grid, i, j) > 0:
                    res += 1
        return res

    def dfs(self, grid, x, y):
        if (x < 0) or (x >= self.m) or (y < 0) or (y >= self.n) or grid[x][y] == '0':
            return 0
        grid[x][y] = '0'
        area = 1
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            area += self.dfs(grid, x + dir[0], y + dir[1])
        return area


if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    obj = Solution()
    print(obj.numIslands(grid))