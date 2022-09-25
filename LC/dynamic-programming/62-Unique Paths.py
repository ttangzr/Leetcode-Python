# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/10 9:28 AM

class Solution:
    def uniquePaths(self, m: int, n: int):
        # method-1: DP
        # dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        # 第一行，只能往右走
        # 第一列，只能往下走
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    obj = Solution()
    m = 3
    n = 7
    print(obj.uniquePaths(m, n))