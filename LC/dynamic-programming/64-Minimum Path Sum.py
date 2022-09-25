# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/10 8:51 AM

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]):
        # method-1: DP
        # dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # boundary
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    obj = Solution()
    # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # grid = [[1, 2, 3], [4, 5, 6]]
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(obj.minPathSum(grid))