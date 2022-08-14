# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 21:36

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 思路：验证如栈序列是否等于出栈序列
        if len(pushed) != len(popped):
            return False
        n = len(pushed)
        i, j = 0, 0
        stack = []
        while i < n:
            # 入栈
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                # 出栈
                stack.pop()
                j += 1
            i += 1
        return j == n


if __name__ == '__main__':
    obj = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(obj.validateStackSequences(pushed, popped))
