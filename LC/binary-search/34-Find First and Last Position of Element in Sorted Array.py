#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/27 9:46 下午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 34-Find First and Last Position of Element in Sorted Array.py
# @Software: PyCharm

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binary_search_repeat(nums, target)
        last = self.binary_search_repeat(nums, target + 1) - 1
        if first >= len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            return [first, max(first, last)]

    def binary_search_repeat(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == "__main__":
    obj = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8    # [3,4]
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 11      # [-1, -1]
    print(obj.searchRange(nums, target))
