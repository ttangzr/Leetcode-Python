#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # method-1: DP+bit operation
        ret = [0] * (n + 1)
        for i in range(1, n +1):
            ret[i] = ret[i & (i - 1)] + 1
        return ret


if __name__ == "__main__":
    obj = Solution()
    n = 5
    print(obj.countBits(n))