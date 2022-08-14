# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 15:50


from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        d = 0
        while queue:
            r, c, d = queue.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r, new_c = r + dx, c + dy
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c, d + 1))
        if any(1 in r for r in grid):
            return -1
        return d


if __name__ == '__main__':
    obj = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(obj.orangesRotting(grid))