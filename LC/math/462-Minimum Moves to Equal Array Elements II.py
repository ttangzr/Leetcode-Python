# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/9/7 21:25

from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # method-1: sort + find median
        n = len(nums)
        median = self.quick_sort(nums, 0, n - 1, n // 2)
        res = 0
        for num in nums:
            res += abs(num - median)
        return res

    def quick_sort(self, nums, left, right, k):
        q = self.partition(nums, left, right)
        if q == k:
            return nums[q]
        elif q > k:
            return self.quick_sort(nums, left, q - 1, k)
        else:
            return self.quick_sort(nums, q + 1, right, k)

    def partition(self, nums, left, right):
        import random
        rand_idx = random.randint(left, right)
        nums[left], nums[rand_idx] = nums[rand_idx], nums[left]

        pivot = nums[left]
        lt = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
        nums[left], nums[lt] = nums[lt], nums[left]
        return lt


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 10, 2, 9]
    print(obj.minMoves2(nums))
