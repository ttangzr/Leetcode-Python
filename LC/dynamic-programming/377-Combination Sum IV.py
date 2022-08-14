# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/8 10:37 AM


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # method-1: DP
        # 完全背包问题， 涉及顺序，物品放最内层循环
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, target + 1):
            for num in nums:
                if j >= num:
                    dp[j] += dp[j - num]
        return dp[target]


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3]
    target = 4
    print(obj.combinationSum4(nums, target))