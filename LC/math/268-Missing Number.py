#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # method-1: XOR
        # nums: 0  1  3  4
        # idx:  0  1  2  3
        res = len(nums)
        for idx, num in enumerate(nums):
            res ^= idx ^ num
        return res

        # method-2: Sum
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


if __name__ == "__main__":
    # nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    nums = [0, 1, 3]
    obj = Solution()
    print(obj.missingNumber(nums))