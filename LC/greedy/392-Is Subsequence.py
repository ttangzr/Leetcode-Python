#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # method-1: greedy/double-pointer
        s_len = len(s)
        t_len = len(t)
        s_ptr = t_ptr = 0
        while s_ptr < s_len and t_ptr < t_len:
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == s_len

        # method-2: DP
        # f[i][j]: 从位置i开始，字符j第一次出现的位置，m表示后续不存在字符j
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True


if __name__ == '__main__':
    obj = Solution()
    s = "abc"
    t = "ahbgdc"
    print(obj.isSubsequence(s, t))