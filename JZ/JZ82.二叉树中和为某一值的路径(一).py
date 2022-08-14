# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/24 8:19 PM
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        # method-1: DFS
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left, sum - root.val) \
            if root.left else False
        right = self.hasPathSum(root.right, sum - root.val) \
            if root.right else False
        return left or right
