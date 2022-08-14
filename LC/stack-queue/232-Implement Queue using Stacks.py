#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 8:25 上午
# @Author  : T-
# @Site    : 
# @File    : 232-Implement Queue using Stacks.py
# @Software: PyCharm

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        val = self.stack1.pop()
        self.stack1.append(val)
        return val

    def empty(self) -> bool:
        return not self.stack1


if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())