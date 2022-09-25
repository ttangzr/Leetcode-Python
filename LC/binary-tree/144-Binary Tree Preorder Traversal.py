#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:20

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        # method-1: BFS
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            # 先右后左，保证左先遍历
            stack.append(node.right)
            stack.append(node.left)
        return res

        # method-2: DFS
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        res = []
        preorder(root)
        return res


