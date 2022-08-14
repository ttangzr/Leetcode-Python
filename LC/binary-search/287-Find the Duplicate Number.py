#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 8:38 上午
# @Author  : T-
# @Site    : 
# @File    : 287-Find the Duplicate Number.py
# @Software: PyCharm

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # method-1: 快慢指针（Floyd判圈算法/龟兔赛跑算法）
        # # 建立i->nums[i]
        # # 2(a+b)=a+b+kL -> a=(k-1)L+c
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # 快指针从相遇点出发，慢指针从原点出发
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        # 环入口就是答案
        return slow

        # method-2: 二分查找
        # 使cnt[i]为nums中小于等于i的个数，具有单调性
        # [1,3,4,2,2]
        # nums=[1, 2, 3, 4]
        # cnt =[1, 3, 4, 5]
        n = len(nums)
        l, r = 1, n - 1
        ans = -1
        while l <= r:
            mid = (l + r) >> 1
            cnt = 0
            for i in range(n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [1,3,4,2,2]
    print(obj.findDuplicate(nums))