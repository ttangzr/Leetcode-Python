# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/1 10:05 AM


from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # method-1: DP, 完全背包，最值问题(自底而上)
        # dp[j] = min{dp[j], dp[j - cj] + 1}
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

        # method-2:记忆化搜索(自定而下)
        # dp[amount] = min(dp[amount],dp[amount-coin] + 1)
        @lru_cache(None)
        def dfs(amount):
            if amount == 0: return 0
            if amount < 0: return -1  # 无法完成组合
            res = float('inf')
            for coin in coins:
                sub = dfs(amount - coin)
                if sub >= 0:
                    res = min(res, sub + 1)
            return res if res != float('inf') else -1
        res = dfs(amount)
        return res if res != float('inf') else -1


if __name__ == '__main__':
    obj = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(obj.coinChange(coins, amount))