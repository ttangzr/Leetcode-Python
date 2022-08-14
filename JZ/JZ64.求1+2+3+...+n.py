# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 8:56 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Sum_Solution(self , n: int) -> int:
        # write code here
        # method-1: bit operation
        return int((n ** 2 + n) >> 1)


if __name__ == '__main__':
    obj = Solution()
    n = 5
    print(obj.Sum_Solution(n))