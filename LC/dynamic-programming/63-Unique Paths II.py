# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/22 19:39

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # method-1: DP
        # dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        # 初始化第一行和第一列，如果遇到obstacle则后续的都不通
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    obj = Solution()
    obstacleGrid = [[0,1,0],[0,0,0],[0,0,0]]
    print(obj.uniquePathsWithObstacles(obstacleGrid))
