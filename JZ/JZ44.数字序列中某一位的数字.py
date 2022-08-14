# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/27 9:27 AM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def findNthDigit(self , n: int) -> int:
        # write code here
        # 0
        # 1 - 9    | digit = 1 cnt = 9
        # 10 - 99  | digit = 2 cnt = 180
        digit_cnt = 1
        bottom, top = 0, 10
        while n > (top - bottom) * digit_cnt:
            n -= (top - bottom) * digit_cnt
            digit_cnt += 1
            bottom, top = top, top * 10
        num, r = divmod(n, digit_cnt)
        return int(str(num + bottom)[r])


if __name__ == "__main__":
    obj = Solution()
    n = 13
    print(obj.findNthDigit(n))