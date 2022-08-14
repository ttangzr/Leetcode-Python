# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/24 10:20 AM


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # method-1: DP
        # 存在问题
        # [0,i]取若干个整数等于j
        # j >= num: dp[i][j] = dp[i-1][j] | dp[j-num][j]
        # j < num: dp[i][j] = dp[i-1][j]
        # dp[i][0] = True，不需要选，就能满足要求
        # dp[1][nums[0]] = True, 只有nums[0]可选
        total = sum(nums)
        n = len(nums)
        W = total // 2
        if total % 2 or n < 2 or max(nums) > W:
            return False
        dp = [[True] + [False] * W for _ in range(n + 1)]
        dp[1][nums[0]] = True
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(1, W + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][W]

        # method-2: DP(opt)
        # 存在问题，逆序
        # dp[j] = dp[j] | dp[j-num]
        total = sum(nums)
        n = len(nums)
        if total % 2 or n < 2:
            return False
        W = total // 2
        dp = [True]+ [False] * W
        for i, num in enumerate(nums):
            for j in range(W, num - 1, -1): # j >= num
                dp[j] |= dp[j - num]
        return dp[W]


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 5, 11, 5]
    print(obj.canPartition(nums))