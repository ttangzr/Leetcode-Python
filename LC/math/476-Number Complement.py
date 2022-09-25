#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


class Solution:
    def findComplement(self, num: int) -> int:
        # method-1: highbit
        highbit = 0
        for i in range(1, 30 + 1):
            # 找到最高位1的位置
            if num >= (1 << i):
                highbit = i
            else:
                break
        mask = (1 << (highbit + 1)) - 1
        return num ^ mask


if __name__ == "__main__":
    obj = Solution()
    num = 5
    print(obj.findComplement(num))
