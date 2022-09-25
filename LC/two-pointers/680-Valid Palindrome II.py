#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


class Solution:
    def validPalindrome(self, s: str) -> bool:
        first, second = 0, len(s) - 1
        while first < second:
            if s[first] != s[second]:
                return self.isPalindrome(s, first, second - 1) or \
                       self.isPalindrome(s, first + 1, second)
            first += 1
            second -= 1
        return True

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    obj = Solution()
    s = "abca"
    print(obj.validPalindrome(s))