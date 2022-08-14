# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/09 11:11 PM

from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # method-1: in-place hash
        n = len(nums)
        for i in range(n):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                self.swap(nums, i, nums[i])
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    obj = Solution()
    print(obj.findRepeatNumber(nums))
