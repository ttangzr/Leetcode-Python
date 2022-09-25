#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:19

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 2, 3, 3, 4, 4, 8, 8]  # 2
    # nums =  [3,3,7,7,10,11,11]  # 10
    print(obj.singleNonDuplicate(nums))