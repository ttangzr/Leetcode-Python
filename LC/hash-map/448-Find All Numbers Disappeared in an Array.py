# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/07 11:43 PM

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # method-1: in-place hash
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)
        return [i + 1 for i, num in enumerate(nums) if nums[i] - 1 != i]
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        
        
if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    obj = Solution()
    print(obj.findDisappearedNumbers(nums))
