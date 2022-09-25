#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return (a & (a + 1)) == 0


if __name__ == "__main__":
    obj = Solution()
    n = 11
    print(obj.hasAlternatingBits(n))