# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 10:49 AM
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
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int):
        # write code here
        # method-1: DFS
        curr = root
        while True:
            if p < curr.val and q < curr.val:
                # both in left subtree
                curr = curr.left
            elif p > curr.val and q > curr.val:
                # both in right subtree
                curr = curr.right
            else:
                break
        return curr.val
