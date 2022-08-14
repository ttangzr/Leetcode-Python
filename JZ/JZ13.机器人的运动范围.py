# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/1 8:57 PM
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param threshold int整型
# @param rows int整型
# @param cols int整型
# @return int整型
#
class Solution:
    def __init__(self):
        self.threshold = 0
        self.rows, cols = 0, 0
        self.cnt = 0

    def movingCount(self , threshold: int, rows: int, cols: int) -> int:
        # write code here
        # method-1: backtracking
        self.threshold = threshold
        self.rows, self.cols = rows, cols
        matrix = [[0] * cols for _ in range(rows)]
        self.backtracking(matrix, 0, 0)
        return self.cnt

    def backtracking(self, matrix, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols \
                or self.check(i) + self.check(j) > self.threshold \
                or matrix[i][j] == 1:
            return
        self.cnt += 1
        matrix[i][j] = 1
        for dir in [(1, 0), (0, 1)]:
            self.backtracking(matrix, i + dir[0], j + dir[1])

    def check(self, n):
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        return sum


if __name__ == '__main__':
    obj = Solution()
    # threshold, rows, cols = 5,10,10
    threshold, rows, cols = 15, 100, 100
    print(obj.movingCount(threshold, rows, cols))