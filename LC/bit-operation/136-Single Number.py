#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:40 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 136-Single Number.py
# @Software: PyCharm

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num_idx in range(len(nums)):
            res ^= nums[num_idx]
        return res
        # return reduce(lambda x, y: x ^ y, nums)


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    obj = Solution()
    print(obj.singleNumber(nums))