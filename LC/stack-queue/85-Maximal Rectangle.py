#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/14 16:24

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # method-1: 单调栈
        row, col = len(matrix), len(matrix[0])
        if len(matrix) == 0:
            return 0
        heights = [0] * col
        max_rec = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            # 每层更新max_rec
            max_rec = max(max_rec, self.largestRectangleArea(heights))
        return max_rec
        
    # 84.Largest Rectangle in Histogram
    def largestRectangleArea(self, heights: List[int]) -> int:
        _heights = [0] + heights + [0]
        n = len(_heights)
        res = 0
        stack = [0]
        for right_i, right_h in enumerate(_heights):
            while right_h < _heights[stack[-1]]:
                cur_i = stack.pop()
                left_i = stack[-1]
                cur_h = _heights[cur_i]
                cur_w = right_i - left_i - 1
                res = max(res, cur_w * cur_h)
            stack.append(right_i)
        return res
        
        
if __name__ == "__main__":
    obj = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(obj.maximalRectangle(matrix))