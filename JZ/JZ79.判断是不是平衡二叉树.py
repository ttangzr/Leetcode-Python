# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/25 7:23 PM
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
    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        # write code here
        # method-1: DFS
        if not pRoot:
            return True
        return self.dfs(pRoot, 1)[1]

    def dfs(self, root, depth):
        if not root:
            return depth - 1, True
        left_depth, left_blc = self.dfs(root.left, depth + 1)
        right_depth, right_blc = self.dfs(root.right, depth + 1)
        return max(left_depth, right_depth), \
               abs(left_depth - right_depth) <= 1 \
               and left_blc and right_blc