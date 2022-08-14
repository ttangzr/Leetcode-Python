# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/27 3:30 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        # method-1: DP
        if n <= 2:
            return n
        dp_i_1, dp_i_2 = 1, 1
        dp_i = 0
        for i in range(2, n):
            dp_i = dp_i_1 + dp_i_2
            dp_i_1, dp_i_2 = dp_i, dp_i_1
        return dp_i

if __name__ == "__main__":
    obj = Solution()
    n = 4
    print(obj.Fibonacci(n))