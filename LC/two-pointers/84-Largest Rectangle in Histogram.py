# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 23:10


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # method-1: force(timeout)
        # size = len(heights)
        # res = 0
        # for i in range(size):
        #     cur_height = heights[i]
        #     # 左右扩散
        #     left = i
        #     while left > 0 and heights[left - 1] >= cur_height:
        #         left -= 1
        #     right = i
        #     while right < size - 1 and heights[right + 1] >= cur_height:
        #         right += 1
        #     width = right - left + 1
        #     res = max(res, width * cur_height)
        # return res

        # method-2: 单调栈
        size = len(heights)
        res = 0
        # 增加dummy节点
        heights = [0] + heights + [0]
        stack = [0]
        size += 2
        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res


if __name__ == "__main__":
    obj = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(obj.largestRectangleArea(heights))
