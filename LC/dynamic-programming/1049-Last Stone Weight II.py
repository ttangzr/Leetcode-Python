# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/21 15:33

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # method-1: DP, 0-1背包存在问题
        # (sum-neg)-neg=sum-2neg, 要使neg尽量大，最大neg得到结果为最优
        # 背包容量取 sum/2
        # dp[i][j]表示前i个石头能否凑出重量j
        total = sum(stones)
        W = total // 2
        n = len(stones)
        dp = [[False] * (W + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            stone = stones[i - 1]
            for j in range(W + 1):  # 从0开始!
                if j >= stone:
                    dp[i][j] = dp[i - 1][j] | dp[i -1][j - stone]
                else:
                    dp[i][j] = dp[i - 1][j]
        # 找到最大的neg
        res = 0
        for j in range(W, -1, -1):
            if dp[n][j]:
                res = total - 2 * j
                break
        return res

        # method-2: DP (optimized)
        total = sum(stones)
        W = total // 2
        n = len(stones)
        dp = [False] * (W + 1)
        dp[0] = True
        for i in range(1, n + 1):
            stone = stones[i - 1]
            for j in range(W, stone - 1, -1):  # 从0开始!
                dp[j] = dp[j] | dp[j - stone]
        # 找到最大的neg
        res = 0
        for j in range(W, -1, -1):
            if dp[j]:
                res = total - 2 * j
                break
        return res


if __name__ == '__main__':
    obj = Solution()
    # stones = [2, 7, 4, 1, 8, 1]     # 1
    stones = [31,26,33,21,40]       # 5
    print(obj.lastStoneWeightII(stones))