# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/18 9:00 AM


from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # method-1: DFS
        # X X X    X X X
        # X O X -> X A X
        # X O X    X A X
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            self.dfs(board, i, 0)
            self.dfs(board, i, self.n - 1)
        for j in range(self.n):
            self.dfs(board, 0, j)
            self.dfs(board, self.m - 1, j)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, board, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or board[x][y] != "O":
            return
        board[x][y] = "A"
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            self.dfs(board, x + dir[0], y + dir[1])


if __name__ == '__main__':
    obj = Solution()
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "X", "O", "X"]]
    obj.solve(board)
    print(board)
