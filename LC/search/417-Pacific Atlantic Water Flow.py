# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/19 8:51 AM


from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.po = None  # Pacific, top left
        self.ao = None  # Atlantic, bottom right
        self.visited = None
        self.res = list()

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # method-1: DFS+Backtracking
        self.m = len(heights)
        self.n = len(heights[0])
        self.po = [[0] * self.n for _ in range(self.m)]
        self.ao = [[0] * self.n for _ in range(self.m)]

        # Pacific
        self.visited = [[0] * self.n for _ in range(self.m)]
        for j in range(self.n):     # top
            self.dfs(heights, 0, j, True)
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):     # left
            self.dfs(heights, i, 0, True)
        # Atlantic
        self.visited = [[0] * self.n for _ in range(self.m)]
        for j in range(self.n):     # bottom
            self.dfs(heights, self.m - 1, j, False)
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):     # right
            self.dfs(heights, i, self.n - 1, False)

        for i in range(self.m):
            for j in range(self.n):
                if self.po[i][j] == 1 and self.ao[i][j] == 1:
                    self.res.append([i, j])
        return self.res


    def dfs(self, heights, x, y, flag):
        if self.visited[x][y] == 1:
            return
        self.visited[x][y] = 1
        if flag:    # Pacific
            self.po[x][y] = 1
        else:       # Atlantic
            self.ao[x][y] = 1
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x = x + dir[0]
            next_y = y + dir[1]
            if not (0 <= next_x < self.m and 0 <= next_y < self.n):
                continue
            if heights[x][y] > heights[next_x][next_y]:     # 单方向来看流不通
                continue
            self.dfs(heights, next_x, next_y, flag)
        return


if __name__ == '__main__':
    heights = [[1,2,2,3,5],
               [3,2,3,4,4],
               [2,4,5,3,1],
               [6,7,1,4,5],
               [5,1,1,2,4]]
    # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    obj = Solution()
    print(obj.pacificAtlantic(heights))