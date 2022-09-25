#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:18

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
