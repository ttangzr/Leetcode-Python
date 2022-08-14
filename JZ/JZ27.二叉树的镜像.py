# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/23 9:06 PM
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        # method-1: DFS
        if not pRoot:
            return
        return self.dfs(pRoot)

    def dfs(self, root):
        if not root:
            return
        root.left, root.right = self.dfs(root.right), self.dfs(root.left)
        return root
