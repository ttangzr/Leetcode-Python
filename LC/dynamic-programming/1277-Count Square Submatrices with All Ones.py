# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/18 22:20

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # method-1: DP
        # if f[i][j]==1
        # f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
                res += f[i][j]
        return res


if __name__ == '__main__':
    matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]]
    obj = Solution()
    print(obj.countSquares(matrix)) # 15