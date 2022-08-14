# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/4/4 17:04


from typing import List


class Solution:
    def __init__(self):
        self.s = []
        self.res = []

    def generateParenthesis(self, n: int):
        # method-1: backtracking
        self.backtracking(n, 0, 0)
        return self.res

    def backtracking(self, n, left, right):
        if len(self.s) == 2*n:
            self.res.append(''.join(self.s))
        if left < n:
            self.s.append('(')
            self.backtracking(n, left + 1, right)
            self.s.pop()
        if right < left:    # NOTE!
            self.s.append(')')
            self.backtracking(n, left, right + 1)
            self.s.pop()


if __name__ == '__main__':
    obj = Solution()
    n = 3
    print(obj.generateParenthesis(n))