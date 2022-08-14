#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 9:53 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 260-Single Number III.py
# @Software: PyCharm

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]):
        diff = 0
        for num in nums:
            diff ^= num
        diff &= - diff  # 用最后一位1来区分
        res = [0] * 2
        for num in nums:
            if num & diff:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]
    obj = Solution()
    print(obj.singleNumber(nums))