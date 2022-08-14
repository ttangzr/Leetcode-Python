#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 11:30 下午
# @Author  : T-
# @Site    : 
# @File    : 205-Isomorphic Strings.py
# @Software: PyCharm

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if ((s2t.get(x) is not None) and s2t[x] != y) \
                    or ((t2s.get(y) is not None) and t2s[y] != x):
                return False
            s2t[x] = y
            t2s[y] = x
        return True


if __name__ == "__main__":
    obj = Solution()
    s = "paper"
    t = "title"
    print(obj.isIsomorphic(s, t))