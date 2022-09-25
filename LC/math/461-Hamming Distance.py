#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # method-1: bit operation
        res = x ^ y
        count = 0
        while res:
            count += res & 1
            res >>= 1
        return count

        # method-2: Brian Kernighan algorithm
        # n & (n - 1)去除最后一个1
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