#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 10:10 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 342-Power of Four.py
# @Software: PyCharm


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n & (n - 1) == 0 and n > 0 and (n & 0xaaaaaaaa) == 0


if __name__ == "__main__":
    n = 2
    obj = Solution()
    print(obj.isPowerOfFour(n))
