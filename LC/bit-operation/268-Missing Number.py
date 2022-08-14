#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 10:46 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 268-Missing Number.py
# @Software: PyCharm

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # method-1
        for num_idx in range(len(nums) + 1):
            if num_idx not in nums:
                return num_idx

        # method-2: XOR
        # nums: 0  1  3  4
        # idx:  0  1  2  3
        res = len(nums)
        for idx, num in enumerate(nums):
            res ^= idx ^ num
        return res

        # method-3: Sum
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    obj = Solution()
    print(obj.missingNumber(nums))