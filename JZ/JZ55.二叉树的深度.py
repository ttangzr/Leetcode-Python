'''
Description: 
Author: Zhirong
Date: 2022-02-23 09:17:28
LastEditTime: 2022-02-23 18:06:05
LastEditors: Zhirong
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return int整型
#
class Solution:
    def TreeDepth(self , pRoot: TreeNode) -> int:
        # write code here
        # method-1: DFS
        if not pRoot:
            return 0
        lval = self.TreeDepth(pRoot.left)
        rval = self.TreeDepth(pRoot.right)
        return max(lval, rval) + 1

        # method-2: BFS
        if not pRoot:
            return 0
        from collections import deque
        stack = deque([pRoot])
        level = 0
        while stack:
            sz = len(stack)
            while sz:
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                sz -= 1
            level += 1
        return level