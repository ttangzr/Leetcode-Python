# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/07 3:18 AM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # method-1: DFS
        def check(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not check(node.right, node.val, upper):
                return False
            if not check(node.left, lower, node.val):
                return False
            return True
        return check(root)
            
        # method-2: BFS
        if not root:
            return True
        stack, prev = [], float('-inf')
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            cur = node.right
        return True
        
        