#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # method-1: 单调栈
        n = len(nums)
        ans = [0] * n
        stack = []
        nums2 = nums + nums
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > nums[stack[-1]]:
                prev = stack.pop()
                ans[prev] = cur
            if i < n:
                # 第二部分不做append,仅做匹配使用
                stack.append(i)
        for i in stack:
            ans[i] = -1
        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [5,4,3,2,1]
    print(obj.nextGreaterElements(nums))