#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 9:11 上午
# @Author  : T-
# @Site    : 
# @File    : 337-House Robber III.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode):
        # method-1: DFS(超时！->Java/C++)
        if not root:
            return 0
        odd = root.val
        if root.left:
            odd += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            odd += self.rob(root.right.left) + self.rob(root.right.right)
        even = self.rob(root.left) + self.rob(root.right)
        return max(odd, even)

        # method-2: DP
        def _rob(root):
            if not root: return 0, 0
            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)
            # f表示选中root节点的权值，g表示不选中root节点的权值
            # 若选中root，则不能选其左右子节点
            # 若不选中root，则可以选/不选其左右子节点
            f = root.val + ln + rn
            g = max(ls, ln) + max(rs, rn)
            return f, g
        return max(_rob(root))





