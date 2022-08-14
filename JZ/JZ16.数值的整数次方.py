# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/3 8:13 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param base double浮点型
# @param exponent int整型
# @return double浮点型
#
class Solution:
    def Power(self , base: float, exponent: int) -> float:
        # write code here
        # method-1: bit operation
        if exponent < 0:
            base = 1 / base
            exponent = - exponent
        x = base
        res = 1.0
        while exponent:
            if exponent & 1:
                res *= x
            x *= x
            exponent >>= 1
        return res


if __name__ == "__main__":
    obj = Solution()
    base, exponent = 2.0000, 3
    print(obj.Power(base, exponent))