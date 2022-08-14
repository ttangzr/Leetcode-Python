#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 9:17 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 190-Reverse Bits.py
# @Software: PyCharm


class Solution:
    def reverseBits(self, n: int) -> int:
        # method-1: 逐位flip
        ret = 0
        for i in range(32):
            ret |= (n & 1) << (31 - i)
            n >>= 1
        return ret

        # method-2: 分治
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


if __name__ == '__main__':
    nums = 43261596
    obj = Solution()
    print(obj.reverseBits(nums))
