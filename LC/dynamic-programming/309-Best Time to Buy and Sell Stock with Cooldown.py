# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/8 10:59 AM


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method-1: DP (state machine)
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        s1 = [0] * n
        s2 = [0] * n
        buy[0] = s1[0] = - prices[0]
        sell[0] = s2[0] = 0
        for i in range(1, n):
            buy[i] = s2[i - 1] - prices[i]
            s1[i] = max(s1[i - 1], buy[i - 1])
            sell[i] = max(buy[i - 1], s1[i - 1]) + prices[i]
            s2[i] = max(s2[i - 1], sell[i - 1])
        return max(sell[n - 1], s2[n - 1])
    
        # method-2: DP
        # f[i] 表示第i天「结束之后」的累计最大收益
        # f[i][0]: 持有股票
        # f[i][1]: 不持有股票，i天卖出，i+1天处于冷冻期
        # f[i][2]: 不持有股票，不处于冷冻期
        if not prices:
            return 0
        n = len(prices)
        f = [[0] * 3 for _ in range(n)]
        f[0][0], f[0][1], f[0][2] = -prices[0], 0, 0
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
        return max(f[n - 1][1], f[n - 1][2])
    
        # method-2: DP (optimized)
        if not prices:
            return 0
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            new_f0 = max(f0, f2 - prices[i])
            new_f1 = f0 + prices[i]
            new_f2 = max(f1, f2)
            f0, f1, f2 = new_f0, new_f1, new_f2
        return max(f1, f2)


if __name__ == '__main__':
    obj = Solution()
    # prices = [1, 2, 3, 0, 2]
    prices = [6,5,4,1,2,3,0,2]
    print(obj.maxProfit(prices))