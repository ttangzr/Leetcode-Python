#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

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