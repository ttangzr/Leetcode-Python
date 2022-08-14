# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/25 2:52 PM


from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int):
        # method-1: DP
        # 组合问题
        # j >= num, dp[i][j] = dp[i-1][j] + dp[i-1][j-num]
        # j < num, dp[i][j] = dp[i-1][j]
        total = sum(nums)
        n = len(nums)
        if total < target or (total - target) % 2:
            return 0
        # positive - negative = target
        # sum - negative = positive
        # -> sum - target // 2 = negative
        neg = (total - target) // 2
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][neg]

        # method-2: DP(opt)
        # dp[j] += dp[j-num]
        total = sum(nums)
        if total < target or (total - target) % 2:
            return 0
        neg = (total - target) // 2
        dp = [0] * (neg + 1)
        dp[0] = 1
        for i, num in enumerate(nums):
            for j in range(neg, num - 1, -1):   # j >= num
                dp[j] += dp[j - num]
        return dp[neg]

        # method-3: backtracking (timeout!)
        self.backtracking(nums, target, 0, 0)
        return self.count

    def __init__(self):
        self.count = 0

    def backtracking(self, nums, target, nums_sum, index):
        if index == len(nums):
            if nums_sum == target:
                self.count += 1
            return
        else:
            self.backtracking(nums, target, nums_sum + nums[index], index + 1)
            self.backtracking(nums, target, nums_sum - nums[index], index + 1)


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    # nums = [1, 0]
    # target = 1
    print(obj.findTargetSumWays(nums, target))