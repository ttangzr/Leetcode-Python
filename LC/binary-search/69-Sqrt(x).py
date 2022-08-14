#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 9:46 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 69-Sqrt(x).py
# @Software: PyCharm


class Solution:
    def mySqrt(self, x: int) -> int:
        # method-1: binary search
        if x == 0:
            return 0
        l, r, ans = 0, x, -1
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

        # method-2: Newton
        if x == 0:
            return 0
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)


if __name__ == "__main__":
    obj = Solution()
    x = 8
    print(obj.mySqrt(x))
