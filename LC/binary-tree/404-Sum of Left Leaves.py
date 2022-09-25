#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:30

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        # method-1: DFS
        isLeaf = lambda node: not node.left and not node.right
        def dfs(node):
            res = 0
            if node.left:
                res += node.left.val if isLeaf(node.left) else dfs(node.left)
            if node.right and not isLeaf(node.right):
                res += dfs(node.right)
            return res

        if not root:
            return 0
        return dfs(root)

        # method-2: BFS
        if not root:
            return 0
        import collections
        queue = collections.deque([root])
        res = 0
        isLeaf = lambda node: not node.left and not node.right
        while queue:
            node = queue.popleft()
            if node.left:
                if isLeaf(node.left):
                    res += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                if not isLeaf(node.right):
                    queue.append(node.right)
        return res




