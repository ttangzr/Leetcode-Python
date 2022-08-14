# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/13 00:06 AM

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # method-1: sliding window
        # (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        n = len(nums)
        odd = [-1]  # 满足边界个数
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)   # 满足边界个数
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans
        
        # method-2: prefix sum
        # prefix sum: num of odds
        # p[i]
        psum = [0] * (len(nums) + 1)
        psum[0] = 1     # 
        odd, res = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                res += psum[odd - k]
            psum[odd] += 1
        return res
        
        
if __name__ == '__main__':
    # nums = [1,1,2,1,1]  # 2
    # k = 3
    nums = [2,2,2,1,2,2,1,2,2,2]    # 16
    k = 2
    obj = Solution()
    print(obj.numberOfSubarrays(nums, k))