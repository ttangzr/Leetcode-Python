# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 7:51 PM

from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # write code here
        # method-1: binary search
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return False
        row, col = 0, n - 1
        while row < m and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False


if __name__ == "__main__":
    obj = Solution()
    matrix = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target = 10
    print(obj.findNumberIn2DArray(matrix, target))