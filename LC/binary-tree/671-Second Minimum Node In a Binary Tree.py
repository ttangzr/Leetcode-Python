#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = -1

    def findSecondMinimumValue(self, root: TreeNode):
        # method-1: DFS
        # root.val等于两个子节点中较小的一个
        # root一定为最小的，只需要找到严格大于root.val的值
        self.dfs(root, root.val)
        return self.ans

    def dfs(self, node, val):
        if not node:
            return
        # 如果大于等于，则节点及其子节点无需计算直接回溯
        if self.ans != -1 and node.val >= self.ans:
            return
        # 找到严格大于val的值
        if node.val > val:
            self.ans = node.val
        self.dfs(node.left, val)
        self.dfs(node.right, val)



