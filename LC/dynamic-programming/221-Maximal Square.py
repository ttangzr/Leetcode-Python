# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/18 22:08

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # method-1: DP
        # if f[i][j]==1
        # f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '0':
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
                res = max(res, f[i][j] ** 2)
        return res


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    obj = Solution()
    print(obj.maximalSquare(matrix))