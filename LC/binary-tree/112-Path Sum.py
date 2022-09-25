#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/25 21:20

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # method-1:递归
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

        # method-2:BFS
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                # 到达末尾子节点，进行判断
                if val == targetSum:
                    return True
                else:
                    continue
            else:
                # 未到达子节点，继续
                if node.left:
                    stack.append((node.left, node.left.val + val))
                if node.right:
                    stack.append((node.right, node.right.val + val))
        return False




