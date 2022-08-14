#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 2:12 下午
# @Author  : T-
# @Site    : 
# @File    : 513-Find Bottom Left Tree Value.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # method-1: BFS（层次遍历）
        import collections
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val

        # method-2: DFS
        # res第一个值存返回的node.val，第二个存所在层数
        res = [None, -1]
        def dfs(node: TreeNode, level:int):
            if not node.left and not node.right:
                # 更新层数
                if level > res[1]:
                    res[0] = node.val
                    res[1] = level
                return
            # 左边先
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root,0)
        return res[0]
