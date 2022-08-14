#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 11:01 上午
# @Author  : T-
# @Site    : 
# @File    : 235-Lowest Common Ancestor of a Binary Search Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # method-1: 一次遍历
        curr = root
        while True:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                break
        return curr