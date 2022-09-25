#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            if hashMap.get(target - num) is not None:
                return [hashMap.get(target - num), i]
            hashMap[num] = i


if __name__ == "__main__":
    obj = Solution()
    nums = [3, 2, 4]
    target = 6
    print(obj.twoSum(nums, target))