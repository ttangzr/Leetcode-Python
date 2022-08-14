'''
Description: 
Author: Zhirong
Date: 2022-02-23 18:24:23
LastEditTime: 2022-02-23 18:29:38
LastEditors: Zhirong
'''
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
        # method-1: BFS
        if not pRoot:
            return []
        level = 0
        from collections import deque
        stack = deque([pRoot])
        ret = list()
        while stack:
            sz = len(stack)
            res_level = list()
            while sz:
                node = stack.popleft()
                res_level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                sz -= 1
            # reverse if it's odd level
            if level % 2:
                ret.append(res_level[::-1])
            else:
                ret.append(res_level)
            level += 1
        return ret