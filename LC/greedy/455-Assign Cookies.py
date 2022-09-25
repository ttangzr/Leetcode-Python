#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30


from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # method-1: greedy
        # 用最小的饼干优先满足胃口最小的孩子
        g.sort()
        s.sort()
        count = 0
        g_i, s_i = 0, 0
        g_len, s_len = len(g), len(s)
        while g_i < g_len and s_i < s_len:
            while s_i < s_len and g[g_i] > s[s_i]:
                s_i += 1
            if s_i < s_len and g[g_i] <= s[s_i]:
                count += 1
            g_i += 1
            s_i += 1
        return count


if __name__ == "__main__":
    g = [1, 2]
    s = [1, 2, 3]
    obj = Solution()
    print(obj.findContentChildren(g, s))