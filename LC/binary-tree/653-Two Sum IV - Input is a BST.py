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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # method-1: inorder+二分
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        nums = []
        inorder(root)
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                return True
            if sum < k:
                i += 1
            else:
                j -= 1
        return False