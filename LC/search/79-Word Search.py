# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/23 8:48 AM


from typing import List


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def exist(self, board: List[List[str]], word: str):
        # method-1: backtracking
        self.m = len(board)
        self.n = len(board[0])
        visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.backtracking(board, i, j, word, 0, visited):
                    return True
        return False

    def backtracking(self, board, x, y, word, index, visited):
        if index == len(word):
            return True
        if x < 0 or x >= self.m or y < 0 or y >= self.n \
                or board[x][y] != word[index] or visited[x][y]:
            return False

        visited[x][y] = 1
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_x = x + dir[0]
            next_y = y + dir[1]
            if self.backtracking(board, next_x, next_y, word, index + 1, visited):
                return True
        visited[x][y] = 0
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    obj = Solution()
    print(obj.exist(board, word))