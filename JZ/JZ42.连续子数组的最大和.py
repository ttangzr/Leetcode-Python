# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/27 2:32 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型
#
from typing import List
class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        # method-1: DP
        # dp[i] = max(dp[i-1], dp[i-1]+array[i])
        n = len(array)
        dp = [0] * n
        dp[0] = array[0]
        res = array[0]
        for i in range(1, n):
            dp[i] = max(array[i], dp[i - 1] + array[i])
            res = max(res, dp[i])
        return res

        # method-2: DP(optimized)
        dp = 0
        res = array[0]
        for i in range(0, len(array)):
            dp = max(array[i], dp + array[i])
            res = max(res, dp)
        return res


if __name__ == "__main__":
    obj = Solution()
    array = [1,-2,3,10,-4,7,2,-5]
    print(obj.FindGreatestSumOfSubArray(array))