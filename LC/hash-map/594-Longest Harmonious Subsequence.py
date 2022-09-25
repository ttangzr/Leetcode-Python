#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

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