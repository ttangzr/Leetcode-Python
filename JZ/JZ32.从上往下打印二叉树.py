# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/23 9:15 PM
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
# @return int整型一维数组
#
class Solution:
    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
        # method-1: BFS
        if not root:
            return []
        from collections import deque
        stack = deque([root])
        ret = list()
        while stack:
            sz = len(stack)
            while sz:
                node = stack.popleft()
                ret.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                sz -= 1
        return ret