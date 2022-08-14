# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/24 21:28

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        in_root_index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:in_root_index], postorder[:in_root_index])
        root.right = self.buildTree(inorder[in_root_index + 1:], postorder[in_root_index: -1])
        return root
