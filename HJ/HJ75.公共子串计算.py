# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 13:05

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str):
        # method-1: DP
        n1, n2 = len(text1), len(text2)
        maxlen = 0
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                if text1[i1 - 1] == text2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                    maxlen = max(dp[i1][i2], maxlen)
                else:
                    dp[i1][i2] = 0
        return maxlen

if __name__ == '__main__':
    text1 = input()
    text2 = input()
    obj = Solution()
    print(obj.longestCommonSubsequence(text1, text2))