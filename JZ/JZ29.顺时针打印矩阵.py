# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/5 11:50 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
from typing import List

class Solution:
    def printMatrix(self , matrix: List[List[int]]):
        # write code here
        if not matrix:
            return []
        res = []
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while True:
            # left->right
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down:   break
            # up->down
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:    break
            # right->left
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            if up > down:   break
            # down->up
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:    break
        return res


if __name__ == '__main__':
    obj = Solution()
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    print(obj.printMatrix(matrix))
