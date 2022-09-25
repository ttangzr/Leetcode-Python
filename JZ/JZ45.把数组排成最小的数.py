# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/9/13 10:18

from typing import List

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # method-1: sort
        # x + y > y + x: x is larger
        strs = [str(num) for num in nums]
        self.quick_sort(strs, 0, len(strs) - 1)
        return ''.join(strs)

    def quick_sort(self, nums, l, r):
        if l >= r:
            return
        p = self.partition(nums, l, r)
        self.quick_sort(nums, l, p - 1)
        self.quick_sort(nums, p + 1, r)

    def partition(self, nums, left, right):
        import random
        rand_idx = random.randint(left, right)
        nums[rand_idx], nums[left] = nums[left], nums[rand_idx]
        pivot = nums[left]
        lt = left
        for i in range(left + 1, right + 1):
            if pivot + nums[i] > nums[i] + pivot:
                lt += 1
                nums[i], nums[lt] = nums[lt], nums[i]
        nums[left], nums[lt] = nums[lt], nums[left]
        return lt


if __name__ == "__main__":
    obj = Solution()
    nums = [3,30,34,5,9]
    print(obj.minNumber(nums))