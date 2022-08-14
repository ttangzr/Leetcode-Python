# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/3 10:16 AM


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]):
        # method-1: DP(opt)
        # 完全背包，组合问题
        # dp[j] += dp[j - num]
        dp =  [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


if __name__ == '__main__':
    obj = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(obj.change(amount, coins))
