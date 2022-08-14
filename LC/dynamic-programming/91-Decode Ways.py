# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/14 9:02 AM


class Solution:
    def numDecodings(self, s: str) -> int:
        # method-1: DP
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            # i-1单独组成
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # i-1与i-2组成2个
            if i > 1 and s[i - 2] != '0' and int(s[i-2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s = "12"
    obj = Solution()
    print(obj.numDecodings(s))