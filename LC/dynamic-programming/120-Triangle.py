#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/17 14:56

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # method-1: DP
        n = len(triangle)
        if n < 2:
            return triangle[0][0]
        f = list(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] += min(f[i + 1][j], f[i + 1][j + 1])
        return f[0][0]
    
        # method-1: DP (optimized)
        # f[i] is only related to f[i + 1]
        n = len(triangle)
        if n < 2:
            return triangle[0][0]
        f = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[j] = triangle[i][j] + min(f[j], f[j + 1]) 
        return f[0]

        
if __name__ == '__main__':
    obj = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(obj.minimumTotal(triangle))