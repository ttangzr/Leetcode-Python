# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/10 4:38 PM


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method-1: DP
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


if __name__ == '__main__':
    obj = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(obj.maxProfit(prices))