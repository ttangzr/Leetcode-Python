#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 9:12 上午
# @Author  : T-
# @Site    : 
# @File    : 230-Kth Smallest Element in a BST.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # DFS
        # BST的inorder是升序
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res[k-1]

        # BFS
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if not k:
                return cur.val
            cur = cur.right

