# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 8:03 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def NumberOf1(self , n: int) -> int:
        # write code here
        # method-1: bit operation
        ans = 0
        n &= 0xffffffff
        while n:
            ans += 1
            n &= (n - 1)
        return ans


if __name__ == "__main__":
    obj = Solution()
    n = -1
    print(obj.NumberOf1(n))