#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 9:00 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 121-Best Time to Buy and Sell Stock.py
# @Software: PyCharm


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # method-1: greedy
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = max(profit, prices[i] - buy)
        return profit


if __name__ == "__main__":
    obj = Solution()
    # prices = [7,1,5,3,6,4]
    prices = [7, 6, 4, 3, 1]
    print(obj.maxProfit(prices))