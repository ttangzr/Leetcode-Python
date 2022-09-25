#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:20

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):
        # method-1: BFS
        # root->right->left->reverse (前序reverse)
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]

        # method-2: DFS
        def postorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            postorder(root.right)
            postorder(root.left)
        res = []
        postorder(root)
        return res[::-1]

