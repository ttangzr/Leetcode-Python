# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/21 9:32 AM


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # method-1: DP
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                if text1[i1 - 1] == text2[i2 - 1]:
                    dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
        return dp[n1][n2]


if __name__ == "__main__":
    obj = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(obj.longestCommonSubsequence(text1, text2))
