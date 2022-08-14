#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/27 8:59 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 278-First Bad Version.py
# @Software: PyCharm


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l

