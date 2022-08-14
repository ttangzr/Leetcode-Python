#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 9:08 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 476-Number Complement.py
# @Software: PyCharm


class Solution:
    def findComplement(self, num: int) -> int:
        # method-1: XOR with mask
        if num == 0:
            return 1
        mask = 1 << 30
        while num & mask == 0:
            mask >>= 1
        mask = (mask << 1) - 1
        return num ^ mask


if __name__ == "__main__":
    obj = Solution()
    num = 5
    print(obj.findComplement(num))
