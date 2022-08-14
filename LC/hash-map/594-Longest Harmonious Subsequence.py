#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 1:02 下午
# @Author  : T-
# @Site    : 
# @File    : 594-Longest Harmonious Subsequence.py
# @Software: PyCharm

from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashMap = {}
        ans = 0
        for num in nums:
            if hashMap.get(num) is not None:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        for num in hashMap.keys():
            if hashMap.get(num + 1) is not None:
                ans = max(ans, hashMap[num] + hashMap[num + 1])
        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [1,1,1]
    print(obj.findLHS(nums))