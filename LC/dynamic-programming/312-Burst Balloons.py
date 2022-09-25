#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/17 20:53

from typing import List
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # method-1: DFS+记忆化搜索
        n = len(nums)
        val = [1] + nums + [1]
        res = [[-1] * (n + 2) for _ in range(n + 2)]

        # use cache (python>=3.9 is need)
        @lru_cache(None)
        def solve_cache(left, right):
            # 开区间，左右两边不取
            if left + 1 >= right:
                return 0
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                # 分治
                total += solve_cache(left, i) + solve_cache(i, right)
                best = max(best, total)
            return best
        # use array
        def solve(left, right):
            # 开区间，左右两边不取
            if left + 1 >= right:
                return 0
            if res[left][right] != -1:
                return res[left][right]
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                # 分治
                total += solve(left, i) + solve(i, right)
                res[left][right] = max(res[left][right], total)
            return res[left][right]

        return solve(0, n + 1)
    
        # method-2: DP
        # dp[i][j]表示(i,j)能得到的最多的硬币
        # i + 1 < j
        # i + 1 < j < n + 1 -> i < n
        n = len(nums)
        val = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][n + 1]
                

if __name__ == '__main__':
    obj = Solution()
    nums = [3,1,5,8]
    print(obj.maxCoins(nums))