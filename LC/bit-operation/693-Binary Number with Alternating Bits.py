#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 11:35 下午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 693-Binary Number with Alternating Bits.py
# @Software: PyCharm


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return (a & (a + 1)) == 0


if __name__ == "__main__":
    obj = Solution()
    n = 11
    print(obj.hasAlternatingBits(n))