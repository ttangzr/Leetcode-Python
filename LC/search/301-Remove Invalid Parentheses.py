# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/7/24 15:26

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # method-1: backtracking + pruning
        # travel to determine lremove, rrmove
        lremove, rremove = 0, 0
        for ch in s:
            if ch == '(':
                lremove += 1
            elif ch == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1
        self.backtracking(s, 0, lremove, rremove)
        return self.res

        # method-2: BFS
        res = []
        curset = set([s])
        while True:
            for ss in curset:
                if self.isValid(ss):
                    res.append(ss)
            if len(res) > 0:
                return res
            nextset = set()
            for ss in curset:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == ss[i - 1]:
                        continue
                    if ss[i] == '(' or ss[i] == ')':
                        nextset.add(ss[:i] + ss[i + 1:])
            curset = nextset

    def backtracking(self, s, start, lremove, rremove):
        if lremove == 0 and rremove == 0:
            if self.isValid(s):
                self.res.append(s)
            return
        for i in range(start, len(s)):
            # pruning
            if i > start and s[i] == s[i - 1]:
                continue
            # remain s cannot meet the amount
            if lremove + rremove > len(s) - i:
                break
            # remove left
            if lremove > 0 and s[i] == '(':
                self.backtracking(s[:i] + s[i + 1:], i, lremove - 1, rremove)
            # remove right
            if rremove > 0 and s[i] == ')':
                self.backtracking(s[:i] + s[i + 1:], i, lremove, rremove - 1)

    def isValid(self, s):
        # check if s is valid parentheses, i.e., lremove == 0
        lrm = 0
        for ch in s:
            if ch == '(':
                lrm += 1
            elif ch == ')':
                lrm -= 1
                if lrm < 0:
                    return False
        return lrm == 0


if __name__ == '__main__':
    obj = Solution()
    # s = "(a)())()"
    s = "()())()"
    print(obj.removeInvalidParentheses(s))