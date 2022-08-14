'''
Description: 
Author: Zhirong
Date: 2021-05-26 08:53:10
LastEditTime: 2021-05-26 08:58:51
LastEditors: Zhirong
'''

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


if __name__ == "__main__":
    obj = Solution()
    matrix = [[1,2],[2,2]]
    print(obj.isToeplitzMatrix(matrix))