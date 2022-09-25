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
    def getMinimumDifference(self, root: TreeNode) -> int:
        # method-1: inorder
        self.pre = None
        self.min_val = float('inf')
        self.inorder(root)
        return self.min_val

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if self.pre:
            self.min_val = min(self.min_val, node.val - self.pre.val)
        self.pre = node
        self.inorder(node.right)

