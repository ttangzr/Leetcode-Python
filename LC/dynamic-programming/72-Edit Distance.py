# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/14 3:01 PM


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # method-1: DP(opt)
        m, n = len(word1), len(word2)
        if m * n == 0:
            return m + n
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                case1 = dp[i - 1][j] + 1
                case2 = dp[i][j - 1] + 1
                case3 = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    case3 += 1
                dp[i][j] = min(case1, case2, case3)
        return dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    word1 = "horse"
    word2 = "ros"
    print(obj.minDistance(word1, word2))
