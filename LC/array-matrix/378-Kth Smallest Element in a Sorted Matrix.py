#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 12:34 下午
# @Author  : T-
# @Site    : 
# @File    : 378-Kth Smallest Element in a Sorted Matrix.py
# @Software: PyCharm

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 二分查找
        n = len(matrix)
        def check(mid):
            i, j= n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left



if __name__ == "__main__":
    obj = Solution()
    matrix = [[1,3,5],
              [6,7,12],
              [11,14,14]]
    k = 3
    print(obj.kthSmallest(matrix, k))