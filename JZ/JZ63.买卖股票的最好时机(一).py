# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/1 9:05 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
from typing import List
class Solution:
    def maxProfit(self , prices: List[int]) -> int:
        # write code here
        # method-1: DP
        sell = 0
        min_price = 1e5
        for i in range(len(prices)):
            sell = max(sell, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return sell


if __name__ == '__main__':
    obj = Solution()
    prices = [8,9,2,5,4,7,1]
    print(obj.maxProfit(prices))