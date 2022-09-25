# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/8 12:00 PM


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int):
        # method-1: DP (state machine)
        n = len(prices)
        buy = [0] * n
        s1 = [0] * n
        sell = [0] * n
        s2 = [0] * n
        buy[0] = s1[0] = - prices[0]
        sell[0] = s2[0] = 0
        for i in range(1, n):
            buy[i] = max(sell[i - 1], s2[i - 1]) - prices[i]
            s1[i] = max(s1[i - 1], buy[i - 1])
            sell[i] = max(s1[i - 1], buy[i - 1]) - fee + prices[i]
            s2[i] = max(s2[i - 1], sell[i - 1])
        return max(sell[n - 1], s2[n - 1])
    
        # method-2: DP
        if not prices:
            return 0
        n = len(prices)
        f = [[0] * 2 for i in range(n)]
        f[0][0], f[0][1] = -prices[0], 0
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] - prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 1][0] + prices[i] - fee)
        return f[n - 1][1]
    
        # method-3: DP (optimized)
        if not prices:
            return 0
        n = len(prices)
        f0, f1 = -prices[0], 0
        for i in range(1, n):
            new_f0 = max(f0, f1 - prices[i])
            new_f1 = max(f1, f0 + prices[i]- fee)
            f0, f1 = new_f0, new_f1
        return f1


if __name__ == '__main__':
    obj = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(obj.maxProfit(prices, fee))