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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # method-1: DFS
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        left_max = self.dfs(node.left)
        right_max = self.dfs(node.right)
        # 与root.val相等, 则+1, 否则为0
        left = right = 0
        if node.left and node.left.val == node.val:
            left = left_max + 1
        if node.right and node.right.val == node.val:
            right = right_max + 1
        self.ans = max(self.ans, left + right)
        return max(left, right)



