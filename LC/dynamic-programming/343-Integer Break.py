# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/13 8:40 AM


class Solution:
    def integerBreak(self, n: int) -> int:
        # method-1: DP
        # dp[i] = max{j*(i-j), j*dp[i-j]}
        # dp[0] = dp[1] = 0
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


if __name__ == '__main__':
    n = 10
    obj = Solution()
    print(obj.integerBreak(n))