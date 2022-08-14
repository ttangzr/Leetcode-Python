#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 12:19 下午
# @Author  : T-
# @Site    : 
# @File    : 697-Degree of an Array.py
# @Software: PyCharm

from typing import  List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # method-1: hashmap(count, left, right)
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                map[num][0] += 1
                map[num][2] = i
            else:
                map[num] = [1, i, i]

        maxNum = minLen = 0
        for count, left, right in map.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                if minLen > right - left + 1:
                    minLen = right - left + 1
        return minLen


if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,2,3,1,4,2]
    print(obj.findShortestSubArray(nums))

