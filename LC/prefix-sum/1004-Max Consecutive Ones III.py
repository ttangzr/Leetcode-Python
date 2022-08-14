# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/3 16:44

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # method-1: prefix + binary search
        # prefix: p[r] - p[l - 1] >= k -> p[l - 1] >= p[r] - k
        # prefix是单调的，有重复元素的
        n = len(nums)
        p = [0] * (n + 1)   # start with 1
        # l-1从0开始
        for i in range(1, n + 1):
            p[i] = p[i - 1] + (1 - nums[i - 1])
        ans = 0
        for right in range(n):
            left = self.binary_search(p, p[right + 1] - k)
            ans = max(ans, (right + 1) - (left + 1) + 1)
        return ans

        # method-2: sliding window
        n = len(nums)
        left = lsum = rsum = 0
        ans = 0
        for right in range(n):
            rsum += 1 - nums[right]
            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


    def binary_search(self, p, target):
        # 有重复元素，查找最左边的target
        l, r = 0, len(p)
        while l < r:
            mid = (l + r) >> 1
            if p[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l



if __name__ == '__main__':
    obj = Solution()
    # nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    # K = 3
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    print(obj.longestOnes(nums, K))