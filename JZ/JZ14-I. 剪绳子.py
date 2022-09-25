# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/9/13 11:36

class Solution:
    def cuttingRope(self, n: int) -> int:
        # method-1: DP
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j],
                            dp[j] * (i - j), dp[j] * dp[i - j])
        return dp[n]


if __name__ == '__main__':
    obj = Solution()
    n = 10
    print(obj.cuttingRope(n))