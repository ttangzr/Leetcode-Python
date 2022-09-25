# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/8/22 21:47

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 水平翻转
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
        # 主对焦翻转
        for i in range(n):
            for j in range(n - 1 - i, -1, -1):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]


if __name__ == '__main__':
    obj = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    obj.rotate(matrix)
    print(matrix)