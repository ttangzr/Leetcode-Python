# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/1 8:02 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix char字符型二维数组
# @param word string字符串
# @return bool布尔型
#
from typing import List


class Solution:
    def __init__(self):
        self.n, self.m = 0, 0

    def hasPath(self , matrix: List[List[str]], word: str):
        # write code here
        # method-1: backtracking
        self.n, self.m = len(matrix), len(matrix[0])
        if self.n == 0 or self.m == 0:
            return False
        for i in range(self.n):
            for j in range(self.m):
                if self.backtracking(matrix, i, j, word, 0):
                    return True
        return False

    def backtracking(self, matrix, i, j, word, start):
        if i < 0 or i >= self.n or j < 0 or j >= self.m \
                or matrix[i][j] != word[start]:
            return False
        if start == len(word) - 1:
            return True
        tmp = matrix[i][j]
        matrix[i][j] = '.'
        res = False
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            res |= self.backtracking(matrix, i + dir[0],
                                     j + dir[1], word, start + 1)
        matrix[i][j] = tmp
        return res


if __name__ == '__main__':
    matrix = [['a','b','c','e'],
              ['s','f','c','s'],
              ['a','d','e','e']]
    word = "abcb"
    obj = Solution()
    print(obj.hasPath(matrix, word))
