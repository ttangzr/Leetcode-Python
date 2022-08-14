#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 2:18 下午
# @Author  : T-
# @Site    : 
# @File    : 485-Max Consecutive Ones.py
# @Software: PyCharm

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt = 0
        maxCnt = 0
        for num in nums:
            if num:
                cnt += 1
            else:
                cnt = 0
            maxCnt = max(cnt, maxCnt)
        return maxCnt


if __name__ == "__main__":
    obj = Solution()
    nums = [1,1,0,1,1,1,0,1,1]
    print(obj.findMaxConsecutiveOnes(nums))