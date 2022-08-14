#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/2 9:20 上午
# @Author  : T-
# @Site    : 
# @File    : 94-Binary Tree Inorder Traversal.py
# @Software: PyCharm

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # method-1: DFS
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        res = []
        inorder(root)
        return res

        # method-2: BFS
        res = []
        if not root:
            return res
        stack = []
        cur = root
        # 先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res



