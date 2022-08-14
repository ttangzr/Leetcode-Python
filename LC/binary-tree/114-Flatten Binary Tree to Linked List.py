# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/19 14:53
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        # method-1: preorder
        if not root:
            return
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            preorder.append(node)
            stack.append(node.right)
            stack.append(node.left)
        for i in range(1, len(preorder)):
            prev, curr = preorder[i - 1], preorder[i]
            prev.left = None
            prev.right = curr

        # method-2: find prev
        curr = root
        while curr:
            if curr.left:
                # pre, nex先到左子输
                pre = nex = curr.left
                # 寻找最右节点
                while pre.right:
                    pre = pre.right
                # 右子树接到pre
                pre.right = curr.right
                # 将左子树接到右边
                curr.left = None
                curr.right = nex
            curr = curr.right

