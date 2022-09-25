# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/19 23:40

from functools import lru_cache

class Solution:
    def countDigitOne(self, n: int) -> int:
        # method-1: 数位DP
        digs = []
        while n:
            digs.append(n % 10)
            n //= 10
        digs.append(n)
        dp = [[-1] * (1 << 10) for _ in range(len(digs))]

        # use array
        def dfs(pos, count, limit):
            if pos < 0:
                return count
            if not limit and dp[pos][count] != -1:
                return dp[pos][count]
            ans = 0
            up = digs[pos] if limit else 9
            for i in range(up + 1):
                if i == 1:
                    ans += dfs(pos - 1, count + 1, limit and digs[pos] == i)
                else:
                    ans += dfs(pos - 1, count, limit and digs[pos] == i)
            if not limit:
                dp[pos][count] = ans
            return ans

        # use cache
        @lru_cache(None)
        def dfs_cache(pos, count, limit):
            if pos < 0:
                return count
            ans = 0
            up = digs[pos] if limit else 9
            for i in range(up + 1):
                if i == 1:
                    ans += dfs(pos - 1, count + 1, limit and digs[pos] == i)
                else:
                    ans += dfs(pos - 1, count, limit and digs[pos] == i)
            return ans

        return dfs(len(digs) - 1, 0, True)


if __name__ == '__main__':
    obj = Solution()
    n = 13
    print(obj.countDigitOne(n))