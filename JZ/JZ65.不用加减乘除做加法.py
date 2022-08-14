# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 7:27 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num1 int整型
# @param num2 int整型
# @return int整型
#
class Solution:
    def Add(self , num1: int, num2: int) -> int:
        # write code here
        # method-1: bit operation
        x = 0xFFFFFFFF
        a, b = num1 & x, num2 & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == "__main__":
    obj = Solution()
    num1, num2 = 1, 2
    print(obj.Add(num1, num2))