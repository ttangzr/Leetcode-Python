# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/1 1:32 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self , nums: str) -> int:
        # write code here
        # method-1: DP
        if nums[0] == '0':
            return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if nums[i] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(nums[i - 1: i + 1]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[n - 1]

        # method-2: backtracking (timeout!)
        return self.backtracking(nums, 0)

    def backtracking(self, nums, start):
        if start == len(nums):
            return 1
        if nums[start] == '0':
            return 0
        # decode 1 at once
        res1 = self.backtracking(nums, start + 1)
        res2 = 0
        if start < len(nums) - 1:
            if nums[start] == '1' or \
                (nums[start] == '2' and nums[start + 1] <= '6'):
                res2 = self.backtracking(nums, start + 2)
        return res1 + res2


if __name__ == "__main__":
    obj = Solution()
    nums = "31717126241541717"
    print(obj.solve(nums))