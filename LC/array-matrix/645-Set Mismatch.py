#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 11:24 下午
# @Author  : T-
# @Site    : 
# @File    : 645-Set Mismatch.py
# @Software: PyCharm

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # method-1: 排序+检查相邻是否差1
        nums = sorted(nums)
        dup, truth = -1, 1
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                truth = nums[i - 1] + 1
        return [dup, len(nums) if nums[len(nums) - 1] != len(nums) else truth]

        # method-2: HashMap
        hashMap = {}
        dup, truth = -1, -1
        for i in range(len(nums)):
            if hashMap.get(nums[i]) is not None:
                dup = nums[i]
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        for i in range(len(nums)):
            if hashMap.get(i + 1) is not None:
                if hashMap[i + 1] == 2:
                    dup = i + 1
            else:
                truth = i + 1
        return [dup, truth]

        # method-3: XOR



if __name__ == "__main__":
    obj = Solution()
    # nums = [3,2,3,4,6,5]
    # nums = [1,3,3,4]
    # nums = [1,2,2,4]
    # nums = [2,2]
    nums = [1,1]
    print(obj.findErrorNums(nums))

