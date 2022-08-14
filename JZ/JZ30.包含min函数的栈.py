# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 12:22 PM
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.min_stack = list()
        self.stack = list()

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        else:
            if node <= self.min_stack[-1]:
                self.min_stack.append(node)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        # write code here
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.min_stack:
            return self.min_stack[-1]