#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 9:16 上午
# @Author  : ZhirongTang
# @Site    : 
# @File    : 241-Different Ways to Add Parentheses.py
# @Software: PyCharm


from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # method-1: divide-and-conquer
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, ch in enumerate(expression):
            if ch in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


if __name__ == "__main__":
    obj = Solution()
    expression = "2*3-4*5"  # [-34, -14, -10, -10, 10]
    print(obj.diffWaysToCompute(expression))
