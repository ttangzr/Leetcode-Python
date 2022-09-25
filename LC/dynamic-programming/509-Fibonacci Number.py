#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/15 20:51

class Solution:
    def fib(self, n: int) -> int:
        # method-1: DP
        if n < 2:
            return n
        f_n = 0
        f_n_1 = 1
        f_n_2 = 0
        for i in range(2, n + 1):
            f_n = f_n_1 + f_n_2
            f_n_1, f_n_2 = f_n, f_n_1
        return f_n
        
        
if __name__ == '__main__':
    obj = Solution()
    n = 4
    print(obj.fib(n))