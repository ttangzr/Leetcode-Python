# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/13 10:01 AM


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # method-1: DP
        # 两个字符串的不同字符数：m+n-2*公共字符
        # ref to 1143
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        lcs = dp[m][n]
        return m + n - 2 * lcs

        # method-2: DP(opt)
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # word2为空，需要把word1都删掉
        for i in range(1, m + 1):
            dp[i][0] = i
        # word1为空，需要把word2都删掉
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 相等不需要删除
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 不等，取较小删除次数的
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    word1 = "leetcode"
    word2 = "etco"
    print(obj.minDistance(word1, word2))