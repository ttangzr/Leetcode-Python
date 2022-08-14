#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 7:22 下午
# @Author  : T-
# @Site    : 
# @File    : 637-Average of Levels in Binary Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # method-1: BFS
        avgs = []
        import collections
        queue = collections.deque([root])
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avgs.append(total / size)
        return avgs