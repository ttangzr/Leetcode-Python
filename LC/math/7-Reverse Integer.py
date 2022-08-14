# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/12 8:35 PM
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 0x80000000
        if x == 0:
            return 0
        if x < 0:
            negative = True
            x = -x
        else:
            negative = False
        res = list()
        while x:
            res.append(str(x % 10))
            x //= 10
        ret = int(''.join(res))
        if ret < - INT_MAX or ret > INT_MAX - 1:
            return 0
        if negative:
            return - ret
        else:
            return ret


if __name__ == '__main__':
    x = 1534236469
    obj = Solution()
    print(obj.reverse(x))