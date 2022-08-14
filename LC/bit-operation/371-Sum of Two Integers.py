#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 11:04 下午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 371-Sum of Two Integers.py
# @Software: PyCharm


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # sum: a ^ b
        # carry: (a & b) << 1
        MASK = (1 << 32) - 1
        MAX_INT = 1 << (32 - 1)
        a &= MASK
        b &= MASK
        while b:
            carry = a & b
            a ^= b
            b = (carry << 1) & MASK
        return a if a < MAX_INT else ~(a ^ MASK)


if __name__ == '__main__':
    obj = Solution()
    a = -2
    b = -2
    print(obj.getSum(a, b))