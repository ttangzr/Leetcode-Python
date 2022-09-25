# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/9/6 23:50

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # method-1: math
        res = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                res += 1
        return res


if __name__ == "__main__":
    obj = Solution()
    n = 5
    print(obj.trailingZeroes(n))