# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/8 9:12 AM


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # method-1: DP
        # 不偷最后一间: [0, n - 2]
        # 偷最后一间: [1, n - 1]
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob(nums, 0, n - 1), self._rob(nums, 1, n))

    def _rob(self, nums, start, end):
        # dp[i] = max{dp[i-1], dp[i-2]+nums[i]}
        dp_i_2, dp_i_1, dp_i = 0, 0, 0
        for i in range(start, end):
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
            dp_i = max(dp_i_1, dp_i_2 + nums[i])
        return dp_i


if __name__ == '__main__':
    nums = [2, 3, 2]
    obj = Solution()
    print(obj.rob(nums))