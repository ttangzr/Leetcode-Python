#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:18

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # method-1: binary search
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

        # method-2: greedy
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]


if __name__ == '__main__':
    # nums = [3, 4, 5, 1, 2]
    nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [11, 13, 15, 17]
    obj = Solution()
    print(obj.findMin(nums))