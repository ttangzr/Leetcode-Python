#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:20

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode):
        # method-1: DFS
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = float("inf")
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))
        return min_depth + 1

        # method-2: BFS（层次遍历）
        if not root:
            return 0
        from collections import deque
        stack = deque([root])
        level = 0
        while stack:
            sz = len(stack)
            for _ in range(sz):
                node = stack.popleft()
                if not node.left and not node.right:
                    return level + 1
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            level += 1
        return level



