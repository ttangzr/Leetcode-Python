# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/10 5:35 PM


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # method-1: DP
        if not prices:
            return 0
        n = len(prices)
        k = min(k, n // 2)  # pruning
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]
        # boundary
        buy[0][0], sell[0][0] = -prices[0], 0
        for j in range(1, k + 1):
            buy[0][j] = sell[0][j] = float("-inf")

        for i in range(1, n):
            # sell[i][0] = 0
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

        return max(sell[n - 1])

        # method-2: DP (optimized)
        if not prices:
            return 0
        n = len(prices)
        k = min(k, n // 2)
        buy = [0] * (k + 1)
        sell = [0] * (k + 1)

        buy[0], sell[0] = -prices[0], 0
        for j in range(1, k + 1):
            buy[j] = sell[j] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i])
        return max(sell)


if __name__ == '__main__':
    obj = Solution()
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(obj.maxProfit(k, prices))