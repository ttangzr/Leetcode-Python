#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:17

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # method-1: binary search
        n = len(matrix)
        def check(mid):
            # 计算小于mid的个数
            i, j = n - 1, 0
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    # 右移变大
                    cnt += i + 1
                    j += 1
                else:
                    # 上移变小
                    i -= 1
            return cnt >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                # k <= cnt
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