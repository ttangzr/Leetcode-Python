#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 12:50 下午
# @Author  : T-
# @Site    : 
# @File    : 217-Contains Duplicate.py
# @Software: PyCharm

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # method-1
        hashMap = {}
        for i, num in enumerate(nums):
            if hashMap.get(num) is not None:
                return True
            hashMap[num] = i
        return False


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 1, 2, 2,  3, 4]
    print(obj.containsDuplicate(nums))