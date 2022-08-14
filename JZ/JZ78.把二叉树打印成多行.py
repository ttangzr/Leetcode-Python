# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/25 8:48 PM
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
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        # BFS
        if not pRoot:
            return []
        from collections import deque
        stack = deque([pRoot])
        ret = list()
        while stack:
            sz = len(stack)
            tmp = list()
            while sz:
                node = stack.popleft()
                tmp.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
                sz -= 1
            ret.append(tmp)
        return ret

