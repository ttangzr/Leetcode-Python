# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/23 17:08


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # method-1:中心拓展
        start, end = 0, 0
        for i in range(len(s)):
            # 奇数
            s1, e1 = self.extendSubstrings(s, i, i)
            # 偶数
            s2, e2 = self.extendSubstrings(s, i, i + 1)
            if e1 - s1 > end - start:
                start, end = s1, e1
            if e2 - s2 > end - start:
                start, end = s2, e2
        return s[start: end + 1]


    def extendSubstrings(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end - 1


if __name__ == '__main__':
    obj = Solution()
    s = "babad"
    print(obj.longestPalindrome(s))