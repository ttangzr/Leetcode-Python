# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/21 16:24


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method-1: 双指针/循环不变量的理解
        # [0, l)为非零元素, [l, end]为零
        l, r = 0, 0
        while r < len(nums):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1


if __name__ == "__main__":
    obj = Solution()
    nums = [0, 1, 0, 3, 12]
    obj.moveZeroes(nums)
    print(nums)