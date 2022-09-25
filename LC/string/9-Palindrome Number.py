#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # method-1: 中心拓展
        if x < 0:
            return False
        s = str(x)
        length = len(s)
        if length % 2 == 1:     # odd length
            return self.check(s, length // 2 - 1, length // 2 + 1)
        else:                   # even length
            return self.check(s, length // 2 - 1, length // 2)

        # method-2: reserve half of number
        # Mind: use //
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        right = 0
        while x > right:
            right = right * 10 + x % 10
            x //= 10
        return x == right or x == right // 10

    def check(self, s: str, start: int, end: int) -> bool:
        while start >= 0 and end < len(s):
            if not s[start] == s[end]:
                return False
            start -= 1
            end += 1
        return True


if __name__ == "__main__":
    obj = Solution()
    x = 121
    print(obj.isPalindrome(x))