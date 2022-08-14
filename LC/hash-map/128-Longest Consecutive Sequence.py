#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 3:11 下午
# @Author  : T-
# @Site    : 
# @File    : 128-Longest Consecutive Sequence.py
# @Software: PyCharm

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]):
        # method-1: hash table
        if len(nums) == 0:
            return 0
        ht = dict()
        for num in nums:
            ht[num] = 1
        for num in nums:
            self.recursive_search_ht(ht, num)
        return max(ht.values())
    
    def recursive_search_ht(self, ht, num):
        if ht.get(num) is None:
            return 0
        # pruning: cnt>1说明已search过了
        if ht[num] > 1:
            return ht[num]
        cnt = self.recursive_search_ht(ht, num + 1) + 1
        ht[num] = cnt
        return cnt


if __name__ == "__main__":
    obj = Solution()
    nums = [100,4,200,1,3,2]
    print(obj.longestConsecutive(nums))