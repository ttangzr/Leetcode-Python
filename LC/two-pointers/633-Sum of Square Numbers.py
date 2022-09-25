#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


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