#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/17 15:58

from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # method-1: DP
        # 宽度升序，高度降序
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        # 在高度中找最长递增子序列
        heights = [envelopes[i][1] for i in range(n)]
        return self.lengthOfLIS(heights)
        
    def lengthOfLIS(self, nums):
        # greedy + binary search
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                # 寻找较小元素替换
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) >> 1
                    if d[mid] >= num:
                        r = mid - 1
                        loc = mid
                    else:
                        l = mid + 1
                # 替换
                d[loc] = num
        return len(d)
    
        # DP (timeout!)
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        

if __name__ == '__main__':
    obj = Solution()
    envelopes = [[6, 4], [6, 7], [5, 4], [5, 2], [1, 8], [2, 3]]
    print(obj.maxEnvelopes(envelopes))