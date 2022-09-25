# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/20 00:08

from functools import lru_cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # method-1: 数位DP
        # dp[pos][status]:当前从高位到pos位后，已经选取status集合中的数字
        # i加入集合x: x|(1<<i), 判断集合x是否含数字i:x>>i&1
        digs = []
        while n:
            digs.append(n % 10)
            n //= 10
        dp = [[-1] * (1 << 10) for _ in range(len(digs))]
        # use array
        def dfs(pos, status, limit):
            if pos < 0:
                return 1
            if not limit and dp[pos][status] != -1:
                return dp[pos][status]
            ans = 0
            up = digs[pos] if limit else 9
            for i in range(0, up + 1):
                if pos == 0 and status == 0 and i == 0:
                    # 去除掉 0
                    continue
                elif status == 0 and i == 0:
                    # 对于前导0的情况另外处理，0不加入集合中
                    ans += dfs(pos - 1, status, limit and digs[pos] == i)
                elif status >> i & 1 == 0:
                    ans += dfs(pos - 1, status | (1 << i), limit and digs[pos] == i)
            if not limit:
                dp[pos][status] = ans
            return ans
        # use cache
        @lru_cache(None)
        def dfs_cache(pos, status, limit):
            if pos < 0:
                return 1
            ans = 0
            up = digs[pos] if limit else 9
            for i in range(0, up + 1):
                if pos == 0 and status == 0 and i == 0:
                    # 去除掉 0
                    continue
                elif status == 0 and i == 0:
                    # 对于前导0的情况另外处理，0不加入集合中
                    ans += dfs(pos - 1, status, limit and digs[pos] == i)
                elif status >> i & 1 == 0:
                    ans += dfs(pos - 1, status | (1 << i), limit and digs[pos] == i)
            return ans  
        return dfs(len(digs) - 1, 0, True)


if __name__ == '__main__':
    obj = Solution()
    n = 135
    print(obj.countSpecialNumbers(n))