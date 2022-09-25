#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/17 15:42

class Solution:
    def __init__(self):
        self.memo = dict()
    
    def superEggDrop(self, k: int, n: int) -> int:
        # method-1: DP
        return self.dp(k, n)
        
    def dp(self, k, n):
        ans = -1
        if (k, n) not in self.memo:
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                l, h = 1, n
                while l + 1 < h:
                    x = (l + h) // 2
                    t1 = self.dp(k - 1, x - 1)
                    t2 = self.dp(k, n - x)
                    if t1 < t2:
                        l = x
                    elif t1 > t2:
                        h = x
                    else:
                        l = h = x
                ans = 1 + min(max(self.dp(k - 1, x - 1), self.dp(k, n - x))\
                    for x in (l, h))
            self.memo[(k, n)] = ans
        return self.memo[(k, n)]


if __name__ == '__main__':
    k = 3
    n = 14
    obj = Solution()
    print(obj.superEggDrop(k, n))