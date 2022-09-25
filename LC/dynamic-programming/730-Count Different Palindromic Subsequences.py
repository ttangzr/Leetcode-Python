#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/17 20:21

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        # method-1: DP
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[[0] * n for i in range(n)] for _ in range(4)]
        # i = j, s[i] = ch
        for i, ch in enumerate(s):
            dp[ord(ch) - ord('a')][i][i] = 1
        for sz in range(2, n + 1):
            for j in range(sz - 1, n):
                i = j - sz + 1
                for k, ch in enumerate("abcd"):
                    if s[i] == ch and s[j] == ch:
                        dp[k][i][j] = (2 + sum(d[i + 1][j - 1] for d in dp)) % MOD
                    elif s[i] == ch:
                        dp[k][i][j] = dp[k][i][j - 1]
                    elif s[j] == ch:
                        dp[k][i][j] = dp[k][i + 1][j]
                    else:
                        dp[k][i][j] = dp[k][i + 1][j - 1]
        return sum(d[0][n - 1] for d in dp) % MOD
        
        
if __name__ == '__main__':
    obj = Solution()
    s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
    # s = 'bccb'
    print(obj.countPalindromicSubsequences(s))