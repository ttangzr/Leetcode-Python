# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/14 11:41 PM

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # method-1: in-place hash (tag)
        #     [3, 4, -1, 1]
        # --> [3, 4, 5, 1]
        # --> [-3, 4, -5, -3]
        # --> 2
        n = len(nums)
        # 负数变为n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # <=n的变为负数
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        # 寻找第一个>0元素的索引+1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
    
        # method-2: in-place hash (原地哈希)
        # f(nums[i]) = nums[i] - 1
        # => nums[i] = nums[nums[i] - 1]
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        

if __name__ == "__main__":
    obj = Solution()
    nums = [3, 4, -1, 1, 9, -5]
    print(obj.firstMissingPositive(nums))