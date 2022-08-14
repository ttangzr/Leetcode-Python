# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/8 8:51 AM

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # method-1: DP
        # 抢当前num: dp[i] = dp[i-2] + nums[i]
        # 不抢当前num: dp[i] = dp[i-1]
        # dp[i] = max{dp[i-1], dp[i-2]+nums[i]}
        dp_i_2, dp_i_1, dp_i = 0, 0, 0
        for num in nums:
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
            dp_i = max(dp_i_1, dp_i_2 + num)
        return dp_i


if __name__ == '__main__':
    nums = [2,7,9,3,1]
    obj = Solution()
    print(obj.rob(nums))