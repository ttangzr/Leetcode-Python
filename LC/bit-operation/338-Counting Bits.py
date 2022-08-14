#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 9:24 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 338-Counting Bits.py
# @Software: PyCharm

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # method-1: DP:最低设置位
        ret = [0] * (n + 1)
        for i in range(1, n +1):
            ret[i] = ret[i & (i - 1)] + 1
        return ret


if __name__ == "__main__":
    obj = Solution()
    n = 5
    print(obj.countBits(n))