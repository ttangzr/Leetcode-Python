# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/21 10:11

from typing import List
from functools import lru_cache

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # method-1: 数位DP(单独考虑前导0)
        nums = []
        nn = n
        while nn:
            nums.append(nn % 10)
            nn //= 10
        digs = [int(x) for x in digits]
        dp = [-1] * len(nums)
        @lru_cache(None)
        def dfs_each(pos, limit):
            if pos < 0:
                return 1
            ans = 0
            up = nums[pos] if limit else digs[-1]
            for i in digs:
                if i <= up:
                    ans += dfs_each(pos - 1, limit and nums[pos] == i)
                else:
                    break
            return ans
        res = 0
        for i in range(len(nums)):
            # 逐长度计算，不需要考虑前导0，只有最长一位为
            res += dfs_each(i, i == len(nums) - 1)
        return res

        # method-2：数位DP(综合考虑前导0)
        nums = []
        nn = n
        while nn:
            nums.append(nn % 10)
            nn //= 10
        digs = [int(x) for x in digits]
        dp = [-1] * len(nums)
        # use array
        def dfs(pos, limit, lead):
            if pos < 0:
                return 0 if lead else 1
            if not limit and not lead and dp[pos] != -1:
                return dp[pos]
            ans = 0
            up = nums[pos] if limit else digs[-1]
            if lead:
                ans += dfs(pos - 1, False, True)
            for i in digs:
                if i <= up:
                    ans += dfs(pos - 1, limit and nums[pos] == i, False)
                else:
                    break
            if not limit and not lead:
                dp[pos] = ans
            return ans
        # use cache
        @lru_cache(None)
        def dfs_cache(pos, limit, lead):
            if pos < 0:
                return 0 if lead else 1
            ans = 0
            up = nums[pos] if limit else digs[-1]
            if lead:
                ans += dfs(pos - 1, False, True)
            for i in digs:
                if i <= up:
                    ans += dfs(pos - 1, limit and nums[pos] == i, False)
                else:
                    break
            return ans
        return dfs(len(nums) - 1, True, True)


if __name__ == '__main__':
    obj = Solution()
    # digits = ["1", "3", "5", "7"]
    # n = 100
    digits = ["1", "4", "9"]
    n = 1000000000
    print(obj.atMostNGivenDigitSet(digits, n))