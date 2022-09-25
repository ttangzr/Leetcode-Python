# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/13 8:40 AM


class Solution:
    def integerBreak(self, n: int) -> int:
        # method-1: DP
        # for 1<=j<i, dp[i] = max_(1<=j<i){max{j*(i-j), j*dp[i-j]}}
        # dp[0] = dp[1] = 0
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            # travel all j < i
            for j in range(1, i):
                # dp[j] * (i - j), dp[j] * dp[i - j] 可以不考虑?
                # dp[i] = max(dp[i], j * (i - j), j * dp[i - j], dp[j] * (i - j), dp[j] * dp[i - j])
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

        # method-2: 数学归纳
        # f >= 4->2*(f-2) = 2f-4>=f
        if n <= 3:
            return n - 1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res


if __name__ == '__main__':
    n = 10
    obj = Solution()
    print(obj.integerBreak(n))