# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/27 10:16 AM


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # method-1: DP
        # 最值问题
        # j >= num, dp[i][j] = max/min(dp[i-1][j], dp[i-1][j-num]+1)
        # j < num, # j >= num, dp[i][j] = dp[i-1][j]
        strs_0 = [i.count("0") for i in strs]
        strs_1 = [i.count("1") for i in strs]
        length = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]
        for i in range(1, length + 1):
            zeros, ones = strs_0[i - 1], strs_1[i - 1]
            for jm in range(m + 1):
                for jn in range(n + 1):
                    if jm >= zeros and jn >= ones:
                        dp[i][jm][jn] = max(dp[i - 1][jm][jn], dp[i - 1][jm - zeros][jn - ones] + 1)
                    else:
                        dp[i][jm][jn] = dp[i - 1][jm][jn]
        return dp[length][m][n]

        # method-2: DP(opt)
        # 最值问题
        # dp[j] = max/min(dp[j], dp[j - num] + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for jm in range(m, zeros - 1, -1):
                for jn in range(n, ones - 1, -1):
                    dp[jm][jn] = max(dp[jm][jn], dp[jm - zeros][jn - ones] + 1)
        return dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    # strs = ["10", "0001", "111001", "1", "0"]
    # m = 5
    # n = 3
    # strs = ["10", "0", "1"]
    # m = 1
    # n = 1
    strs = ["11111", "100", "1101", "1101", "11000"]
    m = 5
    n = 7
    print(obj.findMaxForm(strs, m, n))