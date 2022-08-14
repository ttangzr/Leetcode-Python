# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/8 12:00 PM


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int):
        # method-1: DP
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


if __name__ == '__main__':
    obj = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(obj.maxProfit(prices, fee))