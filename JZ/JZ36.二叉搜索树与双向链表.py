# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/24 11:23 PM
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def Convert(self , pRootOfTree ):
        # write code here
        # method-1: DFS
        if not pRootOfTree:
            return
        left, right = self.dfs(pRootOfTree)
        return left

    def dfs(self, root):
        if not root:
            return None, None
        # find head and tail of left/right subtrees
        left_l, left_r = self.dfs(root.left)
        right_l, right_r = self.dfs(root.right)
        # connection
        if left_r:
            left_r.right = root
            root.left = left_r
        if right_l:
            right_l.left = root
            root.right = right_l
        # set default head and tail
        if not left_l: left_l = root
        if not right_r: right_r = root
        return left_l, right_r