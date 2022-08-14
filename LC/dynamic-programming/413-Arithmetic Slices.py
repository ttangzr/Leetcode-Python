# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/11 9:05 AM


from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # method-1: DP
        # dp[i] = dp[i-1] + 1
        n = len(nums)
        if n < 3:
            return 0
        dp = [0] * n
        for i in range(2, n):
            if nums[i] + nums[i - 2] == nums[i - 1] * 2:
                dp[i] = dp[i - 1] + 1
        return sum(dp)


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3, 4, 5]
    print(obj.numberOfArithmeticSlices(nums))