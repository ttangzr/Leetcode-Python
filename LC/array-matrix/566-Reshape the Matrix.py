#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:17

from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        # method-1: flatten
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]
        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [[1, 2],[3, 4],[5, 6]]
    r = 2
    c = 3
    print(obj.matrixReshape(nums, r, c))