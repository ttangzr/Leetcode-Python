#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 8:52 上午
# @Author  : T-
# @Site    : 
# @File    : 240-Search a 2D Matrix II.py
# @Software: PyCharm

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col >= 0:
            if  target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False


if __name__ == "__main__":
    obj = Solution()
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(obj.searchMatrix(matrix, target))


