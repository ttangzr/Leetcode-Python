#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:19
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # method-1: DFS
        def check(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)

        return check(root, root)

        # method-2: BFS
        if not root or (not root.left and not root.right):
            return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True