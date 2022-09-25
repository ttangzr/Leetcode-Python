# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/14 11:22 PM

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # method-1: DP
        # f_max[i] = max(f_max[i-1]*num, f_min[i-1]*num, num)
        # f_min[i] = min(f_max[i-1]*num, f_min[i-1]*num, num)
        n = len(nums)
        f_max, f_min = [0] * n, [0] * n
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, n):
            num = nums[i]
            f_max[i] = max(f_max[i - 1] * num, f_min[i - 1] * num, num)
            f_min[i] = min(f_min[i - 1] * num, f_max[i - 1] * num, num)
        return max(f_max)
    
        # method-2: DP (optimized)
        n = len(nums)
        f_max = f_min = nums[0]
        max_res = nums[0]
        for i in range(1, n):
            num = nums[i]
            new_f_max = max(f_max * num, f_min * num, num)
            new_f_min = min(f_min * num, f_max * num, num)
            f_max, f_min = new_f_max, new_f_min
            max_res = max(max_res, f_max)
        return max_res


if __name__ == '__main__':
    obj = Solution()
    nums = [2, 3, -2, 4]
    print(obj.maxProduct(nums))