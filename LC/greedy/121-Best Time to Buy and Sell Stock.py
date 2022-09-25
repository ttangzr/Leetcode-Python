#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


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