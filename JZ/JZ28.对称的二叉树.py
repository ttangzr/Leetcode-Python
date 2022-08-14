# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/25 8:33 PM
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
# @return bool布尔型
#
class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        # write code here
        # method-1: DFS
        return self.dfs(pRoot, pRoot)

    def dfs(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val \
               and self.dfs(l.left, r.right) \
               and self.dfs(l.right, r.left)