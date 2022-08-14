#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 8:51 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 345-Reverse Vowels of a String.py
# @Software: PyCharm


class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"
        n = len(s)
        s = list(s)
        i, j = 0, n -1
        while i < j:
            while i < n and not isVowel(s[i]):
                i += 1
            while j > 0 and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


if __name__ == "__main__":
    obj = Solution()
    s = "leetcode"
    print(obj.reverseVowels(s))
