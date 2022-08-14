# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/11 11:31 PM

from typing import List
import collections

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # method-1: prefix sum + force (timeout!)
        n = len(nums)
        res = 0
        psum = [0] * (n + 1)
        for i in range(1, n + 1):
            psum[i] = psum[i - 1] + nums[i - 1]
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                if (psum[j] - psum[i]) % k == 0:
                    res += 1
        return res
    
        # method-2: prefix sum + hashmap
        # (psum[j] - psum[i]) % k = 0
        # -> psum[j] % k == psum[i] % k
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1  # 初始化0，不需要凑对
        total, res = 0, 0 
        for num in nums:
            total += num
            module = total % k
            res += hashmap[module]
            hashmap[module] += 1
        return res
    
        # method-2: prefix sum + hashmap, 单次统计
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1  # 初始化0，不需要凑对
        total, res = 0, 0 
        for num in nums:
            total += num
            module = total % k
            hashmap[module] += 1
        for cx in hashmap.values():
            res += cx * (cx - 1) // 2
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(obj.subarraysDivByK(nums, k))
