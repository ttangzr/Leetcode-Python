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
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node: TreeNode):
            if not node:
                return None
            elif node.val > high:
                # 剪掉右子树，继续修剪左子树
                return trim(node.left)
            elif node.val < low:
                # 剪掉左子树，继续修剪右子树
                return trim(node.right)
            else:
                # 否则修剪两边
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)