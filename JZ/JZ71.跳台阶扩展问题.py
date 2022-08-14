# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/28 8:33 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloorII(self , number: int) -> int:
        # write code here
        # method-1: DP
        # dp[i] = dp[1] + ... + dp[i - 1]
        dp_i, dp_i_1 = 0, 1
        for i in range(1, number + 1):
            dp_i += dp_i_1
            dp_i_1 = dp_i
        return dp_i