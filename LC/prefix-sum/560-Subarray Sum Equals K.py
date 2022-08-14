# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/21 16:13

from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int):
        # method-1：enumerate (timeout!)
        count = 0
        n = len(nums)
        for i in range(n):
            total = 0
            for start in range(i, n):
                total += nums[start]
                if total == k:
                    count += 1
        return count

        # method-2：prefix sum (timeout!)
        # pre[i] = pre[i-1] + nums[i]
        # [j...i] = k -> pre[i] - pre[j-1] = k -> pre[j-1] = pre[i] - k
        n = len(nums)
        psum = [0] * (n + 1)
        psum[0] = 0
        for i in range(n):
            psum[i + 1] = psum[i] + nums[i]
        count = 0
        for left in range(n):
            for right in range(left, n):
                # [left ... right] = k
                if psum[right + 1] - psum[left] == k:
                    count += 1
        return count

        # method-3: prefix sum + hashmap
        # [j...i] = k -> pre[i] - pre[j-1] = k -> pre[j-1] = pre[i] - k
        n = len(nums)
        hmap = collections.defaultdict(int)
        hmap[0] = 1
        psum, res = 0, 0
        for i in range(n):
            psum += nums[i]
            res += hmap[psum - k]
            hmap[psum] += 1
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [3,4,7,2,-3,1,4,2]
    k = 7
    print(obj.subarraySum(nums, k))
