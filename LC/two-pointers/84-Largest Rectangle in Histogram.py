# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 23:10


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # method-1: force(timeout)
        n = len(heights)
        res = 0
        for i in range(n):
            cur_height = heights[i]
            # 左右扩散
            left = i
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1
            right = i
            while right < n - 1 and heights[right + 1] >= cur_height:
                right += 1
            width = right - left + 1
            res = max(res, width * cur_height)
        return res

        # method-2: 单调栈
        n = len(heights)
        res = 0
        # 左右增加dummy
        heights = [0] + heights + [0]
        # 入栈保持递增，pop时递减计算宽度
        stack = []
        n += 2
        for right_i, right_h in enumerate(heights):
            while stack and right_h < heights[stack[-1]]:
                cur_i = stack.pop()
                left_i = stack[-1]
                cur_h = heights[cur_i]
                cur_w = right_i - left_i - 1
                res = max(res, cur_w * cur_h)
            stack.append(right_i)
        return res


if __name__ == "__main__":
    obj = Solution()
    heights = [2, 1, 6, 5, 2, 3]
    print(obj.largestRectangleArea(heights))
