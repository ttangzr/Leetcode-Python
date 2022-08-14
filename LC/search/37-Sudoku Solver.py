# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/30 9:21 AM


from typing import List


class Solution1:
    def __init__(self):
        self.line = [[False] * 9 for _ in range(9)]
        self.column = [[False] * 9 for _ in range(9)]
        self.block = [[[False] * 9 for _ in range(3)] for __ in range(3)]
        self.valid = False
        self.space = list()

    def solveSudoku(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        # 4 exists in line 2 -> line[2][3] = True
        # method-1: backtracking
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.space.append([i, j])
                else:
                    digit = int(board[i][j]) - 1
                    self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = True
        self.backtracking(0, board)

    def backtracking(self, pos, board):
        if pos == len(self.space):
            self.valid = True
            return

        i, j = self.space[pos]
        for digit in range(9):
            if self.line[i][digit] == self.column[j][digit] == self.block[i // 3][j // 3][digit] == False:
                self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = True
                board[i][j] = str(digit + 1)
                self.backtracking(pos + 1, board)
                self.line[i][digit] = self.column[j][digit] = self.block[i // 3][j // 3][digit] = False
            if self.valid:
                return

class Solution2:
    def __init__(self):
        self.line = [0] * 9
        self.column = [0] * 9
        self.block = [[0] * 3 for _ in range(3)]
        self.valid = False
        self.space = list()

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # method-2: backtracking + bit operation optimize
        # 011000100 indicates 3, 7, 8 exist
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.space.append([i, j])
                else:
                    digit = int(board[i][j]) - 1
                    self.flip(i, j, digit)
        self.backtracking(0, board)

    def flip(self, i, j, digit):
        self.line[i] ^= (1 << digit)
        self.column[j] ^= (1 << digit)
        self.block[i // 3][j // 3] ^= (1 << digit)

    def backtracking(self, pos, board):
        if pos == len(self.space):
            self.valid = True
            return

        i, j = self.space[pos]
        # 001000100 indicates we can backtrack at bit 3, 7
        mask = ~(self.line[i] | self.column[j] | self.block[i // 3][j // 3]) & 0x1ff
        while mask:
            digitMask = mask & (-mask)  # get last 1
            digit = bin(digitMask).count("0") - 1
            self.flip(i, j, digit)
            board[i][j] = str(digit + 1)
            self.backtracking(pos + 1, board)
            self.flip(i, j, digit)
            mask &= (mask - 1)  # remove last 1
            if self.valid:
                return


if __name__ == '__main__':
    obj = Solution2()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    obj.solveSudoku(board)
    print(board)
