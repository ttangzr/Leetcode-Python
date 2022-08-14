# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/9 9:49 AM


from typing import List


class Solution(object):
    def findDerangement(self, n: int):
        # method-1: DP
        # [1, ..., i, ..., n]
        # i和k位置互换，剩下n-2个数错位排序
        # i放在k，k不放在i，相当于剩下n-1个树错位排序
        # dp[i] = (i-1) * dp[i-2] + (i-1) * dp[i-1]
        if n == 1:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = int(((i - 1) * (dp[i - 2] + dp[i - 1])) % (1e9+7))
        return dp[n]


if __name__ == '__main__':
    n = 3
    obj = Solution()
    print(obj.findDerangement(n))