#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 12:29 下午
# @Author  : T-
# @Site    : 
# @File    : 155-Min Stack.py
# @Software: PyCharm


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())