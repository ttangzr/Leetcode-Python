# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/25 8:54 PM
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' \
               + self.Serialize(root.left) + ',' \
               + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        if not s or s[0] == "#":
            return None
        s_list = s.split(',')
        return self.buildTree(s_list)

    def buildTree(self, s_list):
        if len(s_list) <= 0:
            return None
        val = s_list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.buildTree(s_list)
            root.right = self.buildTree(s_list)
        return root