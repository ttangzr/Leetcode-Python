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
        f_max, f_min = list(nums), list(nums)
        for i in range(1, n):
            num = nums[i]
            f_max[i] = max(f_max[i - 1] * num, max(f_min[i - 1] * num, num))
            f_min[i] = min(f_min[i - 1] * num, min(f_max[i - 1] * num, num))
        return max(f_max)


if __name__ == '__main__':
    obj = Solution()
    nums = [2, 3, -2, 4]
    print(obj.maxProduct(nums))