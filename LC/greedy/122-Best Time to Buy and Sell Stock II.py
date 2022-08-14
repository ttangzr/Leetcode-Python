#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 11:24 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 122-Best Time to Buy and Sell Stock II.py
# @Software: PyCharm


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method-1: greedy
        ans = 0
        for i in range(1, len(prices)):
            # 如果持续涨，进行多笔交易相当于进行一笔交易
            # if prices[i] - prices[i - 1] > 0:
            #     ans += prices[i] - prices[i - 1]
            ans += max(0, prices[i] - prices[i-1])
        return ans

        # method-2: DP
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0            # 表示手里没有股票
        dp[0][1] = -prices[0]   # 表示手里有一支股票
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]


if __name__ == "__main__":
    obj = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(obj.maxProfit(prices))
