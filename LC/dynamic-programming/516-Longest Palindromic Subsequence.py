#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/17 19:48

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # method-1: DP
        n = len(s)
        if n < 2:
            return n
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 注意最大在右上角
        return dp[0][n - 1]

        
if __name__ == '__main__':
    obj = Solution()
    s = "bbbab"
    print(obj.longestPalindromeSubseq(s))