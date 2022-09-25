# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/15 9:28 AM

from typing import List
from functools import lru_cache

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        # method-1: DFS
        self.m, self.n = len(grid), len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(grid, i, j) > 0:
                    res += 1
        return res

        # method-2: Disjoint-set
        nr, nc = len(grid), len(grid[0])
        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()

    def dfs(self, grid, x, y):
        if (x < 0) or (x >= self.m) or (y < 0) or (y >= self.n) or grid[x][y] == '0':
            return 0
        grid[x][y] = '0'
        area = 1
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            area += self.dfs(grid, x + dir[0], y + dir[1])
        return area

class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count

if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    obj = Solution()
    print(obj.numIslands(grid))