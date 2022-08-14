#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 8:40 上午
# @Author  : T-
# @Site    : 
# @File    : 242-Valid Anagram.py
# @Software: PyCharm

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method-1: Counter
        from collections import Counter
        return Counter(s) == Counter(t)

        # method-2: sort
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    obj = Solution()
    s = "anagram"
    t = "nagaram"
    print(obj.isAnagram(s, t))