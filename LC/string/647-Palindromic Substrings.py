#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 9:05 上午
# @Author  : T-
# @Site    : 
# @File    : 647-Palindromic Substrings.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.cnt = 0

    def countSubstrings(self, s: str) -> int:
        # method-1: 中心拓展
        for i in range(len(s)):
            self.extendSubstrings(s, i, i)
            self.extendSubstrings(s, i, i + 1)
        return self.cnt

    def extendSubstrings(self, s: str, start: int, end: int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            self.cnt += 1


if __name__ == "__main__":
    obj = Solution()
    s = "aaa"
    print(obj.countSubstrings(s))