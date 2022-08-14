# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/28 8:43 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def rectCover(self , number: int) -> int:
        # write code here
        # method-1: DP
        # dp[i] = dp[i-1] + dp[i-2]
        if number == 0:
            return 0
        dp_i_1, dp_i_2, dp_i = 1, 0, 0
        for i in range(1, number + 1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_1, dp_i_2 = dp_i, dp_i_1
        return dp_i