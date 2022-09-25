# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/21 17:36

from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # method-1: 记忆化搜索
        # dp[i][j]=max(dp[i+1][j],dp[i−1][j],dp[i][j+1],dp[i][j−1],0)+1
        # 要求[i,j][i,j]周围的数比它小，如果没有比它小的，则长度为1
        m, n = len(matrix), len(matrix[0])
        @lru_cache(None)
        def dfs(x, y):
            best = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nex_x, nex_y = x + dx, y + dy
                if 0 <= nex_x < m and 0 <= nex_y < n and \
                        matrix[nex_x][nex_y] > matrix[x][y]:
                    best = max(best, dfs(nex_x, nex_y) + 1)
            return best
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


if __name__ == '__main__':
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    obj = Solution()
    print(obj.longestIncreasingPath(matrix))