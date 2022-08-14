#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 9:27 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 53-Maximum Subarray.py
# @Software: PyCharm


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]):
        # method-1: DP
        # nums[i]加入f[i-1]，或单独为一段
        # f_max[i] = max(f[i-1]+nums[i], nums[i])
        pre_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            pre_sum = max(pre_sum + nums[i], nums[i])
            max_sum = max(max_sum, pre_sum)
        return max_sum

        # method-2: Divide-and-Conquer
        n = len(nums)
        if n == 0:
            return 0
        return self.max_sub_array(nums, 0, n - 1)
    
    def max_sub_array(self, nums, left, right):
        if left >= right:
            return nums[left]
        mid = (left + right) // 2
        return max(self.max_sub_array(nums, left, mid), 
                   self.max_sub_array(nums, mid + 1, right),
                   self.max_cross_array(nums, left, mid, right))
        
    def max_cross_array(self, nums, left, mid, right):
        # start from mid-1->left and mid+1->right
        # get max values from left and right intervals
        # add mid value
        l = mid - 1
        lsum = 0
        lsum_max = 0
        while l >= left:
            lsum += nums[l]
            lsum_max = max(lsum, lsum_max)
            l -= 1
        r = mid + 1
        rsum, rsum_max = 0, 0
        while r <= right:
            rsum += nums[r]
            rsum_max = max(rsum, rsum_max)
            r += 1
        return nums[mid] + lsum_max + rsum_max


if __name__ == "__main__":
    obj = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    print(obj.maxSubArray(nums))