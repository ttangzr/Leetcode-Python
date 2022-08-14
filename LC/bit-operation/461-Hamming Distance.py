#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 9:56 上午
# @Author  : T-
# @Site    : 
# @File    : 461-Hamming Distance.py
# @Software: PyCharm


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # method-1: bitcount (timeout)
        # res = x ^ y
        # count = 0
        # for bit_idx in range((res // 2) + 1):
        #     if (1 << bit_idx) & res:
        #         count += 1
        # return count

        # method-2: 移位
        res = x ^ y
        count = 0
        while res:
            count += res & 1
            res >>= 1
        return count

        # method-3: Brian Kernighan algorithm
        res = x ^ y
        count = 0
        while res:
            res &= res - 1
            count += 1
        return count


if __name__ == "__main__":
    obj = Solution()
    x = 4
    y = 1
    print(obj.hammingDistance(x, y))