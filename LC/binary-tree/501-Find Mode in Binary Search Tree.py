#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 4:20 下午
# @Author  : T-
# @Site    : 
# @File    : 501-Find Mode in Binary Search Tree.py
# @Software: PyCharm

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # method-1: inorder
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            update(node.val)
            inorder(node.right)

        # update Mode
        def update(val: int):
            nonlocal res, base, count, max_count
            if val == base:
                count += 1
            else:
                count = 1
                base = val
            if count == max_count:
                res.append(val)
            if count > max_count:
                max_count = count
                res = [val]

        res = []
        base = count = max_count = 0
        inorder(root)
        return res
