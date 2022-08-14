# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/23 8:20 PM
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot1 TreeNode类
# @param pRoot2 TreeNode类
# @return bool布尔型
#
class Solution:
    def HasSubtree(self , pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # write code here
        # method-1: DFS
        if not pRoot1 or not pRoot2:
            return False
        return self.dfs(pRoot1, pRoot2) \
               or self.HasSubtree(pRoot1.left, pRoot2) \
               or self.HasSubtree(pRoot1.right, pRoot2)

    def dfs(self, r1, r2):
        if not r2:
            return True
        elif not r1:
            return False
        return r1.val == r2.val \
               and self.dfs(r1.left, r2.left) \
               and self.dfs(r1.right, r2.right)