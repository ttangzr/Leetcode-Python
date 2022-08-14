# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/13 9:17 AM


class Solution:
    def numSquares(self, n: int) -> int:
        # method-2: DP
        # x + j * j = i
        # dp[x] + 1 = dp[i]
        # dp[i] = min{dp[i], dp[i - j * j] + 1}
        # 范围[1, sqrt(i)]
        import math
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i       # bad case: all 1
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


if __name__ == '__main__':
    n = 12
    obj = Solution()
    print(obj.numSquares(n))