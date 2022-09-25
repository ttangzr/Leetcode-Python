# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/22 23:21

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # method-1: prefix sum
        n = len(nums)
        # 左右乘积数组
        L, R = [0] * n, [0] * n
        L[0], R[-1] = 1, 1
        for i in range(1, n):
            L[i] = L[i - 1] * nums[i - 1]
            R[n - 1 - i] = R[n - i] * nums[n - i]
        ans = [0] * n
        for i in range(n):
            ans[i] = L[i] * R[i]
        return ans

        # method-2: prefix sum (optimized)
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        # 正顺作为L
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # 逆序作为R
        base = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * base
            base *= nums[i]
        return ans


if __name__ == '__main__':
    nums = [4, 5, 1, 8, 2]
    obj = Solution()
    print(obj.productExceptSelf(nums))