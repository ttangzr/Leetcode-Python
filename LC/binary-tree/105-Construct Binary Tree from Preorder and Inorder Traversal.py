# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/21 16:00


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_idx + 1], inorder[: root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])
        return root


if __name__ == "__main__":
    obj = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(obj.buildTree(preorder, inorder))