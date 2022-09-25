# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/7 8:44 AM


class Solution:
    def climbStairs(self, n: int) -> int:
        # method-1: DP
        # dp[i] = dp[i-1] + dp[i-2]
        if n < 2:
            return n
        dp_i_2, dp_i_1, dp_i = 1, 1, 0
        for i in range(2, n + 1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_1, dp_i_2 = dp_i, dp_i_1
        return dp_i


if __name__ == '__main__':
    n = 3
    obj = Solution()
    print(obj.climbStairs(n))