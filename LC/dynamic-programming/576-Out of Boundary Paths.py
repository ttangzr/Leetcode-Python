# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/21 17:47

from functools import lru_cache

class Solution:
    MOD = 10 ** 9 + 7
    @lru_cache(None)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # method-1: 记忆化搜索
        # 出界
        if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
            return 1
        # 没次数
        if maxMove == 0:
            return 0
        res = 0
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            res = (res + self.findPaths(m, n, maxMove - 1, startRow + dx, startColumn + dy)) % self.MOD
        return res


if __name__ == '__main__':
    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1
    obj = Solution()
    print(obj.findPaths(m, n, maxMove, startRow, startColumn))