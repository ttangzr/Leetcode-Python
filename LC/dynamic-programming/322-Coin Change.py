# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/1 10:05 AM


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # method-1: DP(opt)
        # 完全背包，最值问题
        # dp[j] = min{dp[j], dp[j - cj] + 1}
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    obj = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(obj.coinChange(coins, amount))