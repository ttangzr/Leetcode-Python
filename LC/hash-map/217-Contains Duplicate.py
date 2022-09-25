#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

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