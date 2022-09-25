#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:18

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
