#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:18

from typing import  List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # method-1: hashmap
        # (count, left, right)
        hmap = {}
        for i, num in enumerate(nums):
            if num in hmap:
                hmap[num][0] += 1
                hmap[num][2] = i
            else:
                hmap[num] = [1, i, i]

        maxNum = minLen = 0
        for count, left, right in hmap.values():
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

