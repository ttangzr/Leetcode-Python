# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/27 3:09 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self , number: int) -> int:
        # write code here
        # method-1: DP
        # dp[i] = dp[i - 1] + dp[i - 2]
        if number <= 1:
            return number
        dp = [0] * (number + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]

        # method-2: DP(optimized)
        if number <= 1:
            return number
        dp_i_1, dp_i_2 = 1, 1
        dp_i = 0
        for i in range(2, number + 1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_1, dp_i_2 = dp_i, dp_i_1
        return dp_i


if __name__ == "__main__":
    obj = Solution()
    number = 7
    print(obj.jumpFloor(number))