#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 5:05 下午
# @Author  : T-
# @Site    : 
# @File    : 739-Daily Temperatures.py
# @Software: PyCharm

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]):
        # method-1: stack(超时)
        # res = []
        # flag = 0
        # for t in range(len(T)):
        #     flag = 0
        #     for tt in range(t + 1, len(T)):
        #         if T[tt] > T[t]:
        #             res.append(tt - t)
        #             flag = 1
        #             break
        #     if not flag:
        #         res.append(0)
        # return res

        # method-2: 单调栈
        n = len(T)
        res = [0] * n
        stack = list()
        for i in range(n):
            t = T[i]
            # 保证栈单调
            while stack and t > T[stack[-1]]:
                pre = stack.pop()
                res[pre] = i - pre
            stack.append(i)
        return res


if __name__ == "__main__":
    obj = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # [1, 1, 4, 2, 1, 1, 0, 0]
    print(obj.dailyTemperatures(temperatures))