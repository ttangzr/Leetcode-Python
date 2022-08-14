# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/11 9:48 PM

from typing import List


class Solution:
    def __init__(self):
        self.water = 0

    def trap(self, height: List[int]) -> int:
        # method-1: force (timeout！)
        n = len(height)
        if n <= 2:
            return 0
        res = 0
        def max_height(l, r):
            h = height[l]
            for i in range(l, r + 1):
                h = max(height[i], h)
            return h
        # [1, len - 2]计算存水体积
        for i in range(1, n - 1):
            # 木桶原理，存水高度取决于左右最高中的较矮者
            left_height = max_height(0, i - 1)
            right_height = max_height(i + 1, n - 1)
            curr_height = min(left_height, right_height)
            if curr_height > height[i]:
                res += curr_height - height[i]
        return res

        # method-2: DP
        n = len(height)
        if n <= 2:
            return 0
        left_max = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max = [0] * (n - 1) + [height[-1]]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        ans = sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
        return ans

        # method-3: two pointer
        # height[l] < height[r]->left_max < right_max
        # -> ans += left_max - height[l]
        ans = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans

        # method-4: 单调栈
        # [left, top] -> height[left] ≥ height[top]
        # height[i] > height[top]
        # w: i - left - 1, h: min(height[left], height[right]) - height[top]
        stack = list()
        res = 0
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curr_width = i - left - 1
                # 木桶效应
                curr_height = min(height[left], height[i]) - height[top]
                res += curr_width * curr_height
            stack.append(i)
        return res


if __name__ == "__main__":
    obj = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(obj.trap(height))