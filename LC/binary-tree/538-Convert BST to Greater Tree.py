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
    def convertBST(self, root: TreeNode) -> TreeNode:
        # method-1: RDL为降序
        self.total = 0
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.right)
        self.total += node.val
        node.val = self.total
        self.dfs(node.left)
