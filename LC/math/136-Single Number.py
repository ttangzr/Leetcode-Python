#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # method-1: bit operation
        res = 0
        for num_idx in range(len(nums)):
            res ^= nums[num_idx]
        return res
        # return reduce(lambda x, y: x ^ y, nums)


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    obj = Solution()
    print(obj.singleNumber(nums))