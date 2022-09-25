#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

class Solution:
    def countBinarySubstrings(self, s: str):
        # method-1: 字符分组/双指针
        pre, cur, count = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                pre = cur
                cur = 1 # reset
            if pre >= cur:
                count += 1
        return count

        # method-2: 前后分组/双指针
        cur = 0
        n = len(s)
        last, ans = 0, 0
        while cur < n:
            c = s[cur]
            # count记录当前字符重复次数
            count = 0
            while cur < n and s[cur] == c:
                cur += 1
                count += 1
            # 取上一段和这一段的较小
            ans += min(count, last)
            # last记录上一段重复字符的个数
            last = count
        return ans


if __name__ == "__main__":
    obj = Solution()
    s = "00111011"  # counts={2,3,1,2}
    print(obj.countBinarySubstrings(s))