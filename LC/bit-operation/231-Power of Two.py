#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 9:44 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 231-Power of Two.py
# @Software: PyCharm


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 and n != 0

if __name__ == "__main__":
    n = 0
    obj = Solution()
    print(obj.isPowerOfTwo(n))
