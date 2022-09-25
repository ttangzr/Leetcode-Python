#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 and n != 0

if __name__ == "__main__":
    n = 0
    obj = Solution()
    print(obj.isPowerOfTwo(n))
