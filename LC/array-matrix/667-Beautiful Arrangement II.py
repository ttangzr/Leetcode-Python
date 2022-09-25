#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:18

from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 1.构造等差数列，把 1 到 n - k - 1 赋值结果数组的前面
        res = [0] * n
        for i in range(n - k - 1):
            res[i] = i + 1
        # 2. 构造交错数列，下标从 n - k - 1 开始，数值从 n - k 开始
        # 控制交错变量
        j = 0
        left = n - k
        right = n
        for i in range(n - k - 1, n):
            if j % 2 == 0:
                res[i] = left
                left += 1
            else:
                res[i] = right
                right -= 1
            j += 1
        return res


if __name__ == "__main__":
    obj = Solution()
    n = 6
    k = 3
    print(obj.constructArray(n, k))