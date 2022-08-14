# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/1 9:31 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param grid int整型二维数组
# @return int整型
#
from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.__value_list = list()
        self.value = 0

    def maxValue(self , grid: List[List[int]]):
        # write code here
        # method-2: DP
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            dp[i][0] = 0
        for j in range(n):
            dp[0][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[m][n]

        # method-1: backtracking (timeout!)
        self.m, self.n = len(grid), len(grid[0])
        self.backtracking(grid, 0, 0)
        return self.value

    def backtracking(self, grid, i, j):
        directions = list()
        self.__value_list.append(grid[i][j])
        if i == self.m - 1 and j == self.n - 1:
            self.value = max(self.value, sum(self.__value_list))
            return
        elif i < self.m - 1 and j < self.n - 1:
            directions = [(1, 0), (0, 1)]
        elif i == self.m - 1 and j < self.n - 1:
            directions = [(0, 1)]
        elif i < self.m - 1 and j == self.n - 1:
            directions = [(1, 0)]
        for dir in directions:
            x, y = i + dir[0], j + dir[1]
            self.backtracking(grid, x, y)
            self.__value_list.pop()


if __name__ == "__main__":
    obj = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(obj.maxValue(grid))