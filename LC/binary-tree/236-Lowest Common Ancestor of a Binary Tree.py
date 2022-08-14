#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 8:44 上午
# @Author  : T-
# @Site    : 
# @File    : 236-Lowest Common Ancestor of a Binary Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # method-1: DFS
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        else:
            # 左右子树都有，说明root为公共节点
            return root