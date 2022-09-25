# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/2 8:33 AM

from typing import List

class Solution:
    def duplicate(self , nums: List[int]):
        # write code here
        # method-1: Hash Map
        hashMap = dict()
        for i, num in enumerate(nums):
            if hashMap.get(num) is not None:
                return num
            else:
                hashMap[num] = 1
        return -1

        # method-2: sort
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            else:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:   # swap
                    a, b = nums[i], nums[nums[i]]
                    nums[i] = b
                    nums[a] = a
        return -1

        # method-1: in-place hash
        n = len(nums)
        for i in range(n):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                self.swap(nums, i, nums[i])

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    obj = Solution()
    numbers = [2, 3, 1, 0, 2, 5, 3]
    print(obj.duplicate(numbers))