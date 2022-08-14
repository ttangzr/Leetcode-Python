#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 8:27 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 633-Sum of Square Numbers.py
# @Software: PyCharm


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # method-1: 双指针
        import math
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            power_sum = i ** 2 + j ** 2
            if power_sum == c:
                return True
            elif power_sum > c:
                j -= 1
            else:
                i += 1
        return False
        # method-2:费马平方和定理


if __name__ == "__main__":
    obj = Solution()
    c = 5
    print(obj.judgeSquareSum(c))