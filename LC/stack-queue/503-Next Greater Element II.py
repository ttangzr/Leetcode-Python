#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 8:43 上午
# @Author  : T-
# @Site    : 
# @File    : 503-Next Greater Element II.py
# @Software: PyCharm
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # method-1: 单调栈
        size = len(nums)
        ans = [0] * size
        stack = list()
        nums2 = nums + nums
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > nums[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = cur
            if i <= size - 1:
                stack.append(i)
        # 没找到的置为-1
        for i in stack:
            ans[i] = -1
        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [5,4,3,2,1]
    print(obj.nextGreaterElements(nums))