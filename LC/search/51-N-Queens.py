# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/1/5 8:40 PM


from typing import List


class Solution:
    def __init__(self):
        self.column = list()
        self.diag45 = list()
        self.diag135 = list()
        self.nQueens = list()
        self.ans = list()

    def solveNQueens(self, n: int) -> List[List[str]]:
        # method-1: backtracking
        self.column = [0] * n
        self.diag45 = [0] * (2 * n - 1)
        self.diag135 = [0] * (2 * n - 1)
        self.nQueens = [['.' for _ in range(n)] for _ in range(n)]
        self.backtracking(0, n)
        return self.ans

    def backtracking(self, row, n):
        if row == n:
            ans = list()
            for row in range(n):
                ans.append(''.join(str(self.nQueens[row][x]) for x in range(n)))
            self.ans.append(ans)
            return

        for col in range(n):
            # diag45: r+c
            # diag135: (n-1)-(c-r)
            diag45_idx = row + col
            diag135_idx = (n - 1) - (col - row)
            if self.column[col] or self.diag45[diag45_idx] or self.diag135[diag135_idx]:
                continue
            self.nQueens[row][col] = 'Q'
            self.column[col] = self.diag45[diag45_idx] = self.diag135[diag135_idx] = 1
            self.backtracking(row + 1, n)
            self.column[col] = self.diag45[diag45_idx] = self.diag135[diag135_idx] = 0
            self.nQueens[row][col] = '.'


if __name__ == '__main__':
    obj = Solution()
    n = 4
    print(obj.solveNQueens(n))