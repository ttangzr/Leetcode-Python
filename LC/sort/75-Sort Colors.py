#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method-1: partition
        # all in [0, p0) = 0
        # all in [p0, i) = 1
        # all in [p2, len) = 2
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:   # nums[i] == 2
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1


if __name__ == "__main__":
    obj = Solution()
    nums = [2,0,2,1,1,0,2,2]
    obj.sortColors(nums)
    print(nums)
