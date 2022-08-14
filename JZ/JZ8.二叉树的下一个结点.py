# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/25 7:46 PM
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        # method-1: DFS
        if not pNode:
            return pNode
        # type1: find left corner of right subtree
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # type2: find parent
        while pNode.next:
            root = pNode.next
            if root.left == pNode:
                return root
            pNode = pNode.next
        return None