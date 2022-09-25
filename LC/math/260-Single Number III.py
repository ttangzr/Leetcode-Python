#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]):
        # method-1: bit operation
        diff = 0
        for num in nums:
            diff ^= num
        diff &= - diff  # 留下最后一位1，用最后一位1来区分
        # 3: 0 1 1 -> 0 1 0 在这一堆里面有多对+1个3
        # 5: 1 0 1 -> 0 0 0 在这一堆里面有多对+1个5
        res = [0] * 2
        for num in nums:
            if num & diff:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]
    obj = Solution()
    print(obj.singleNumber(nums))