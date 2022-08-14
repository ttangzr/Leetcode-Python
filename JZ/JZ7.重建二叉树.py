# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/23 7:42 PM
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        # method-1: DFS
        if not pre:
            return None
        # root node
        root = TreeNode(pre[0])
        # root index in vin
        root_idx = vin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1: root_idx + 1], vin[: root_idx])
        root.right = self.reConstructBinaryTree(pre[root_idx + 1:], vin[root_idx + 1:])
        return root