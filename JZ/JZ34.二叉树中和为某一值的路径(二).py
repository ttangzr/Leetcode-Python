# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/24 8:34 PM
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
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def __init__(self):
        self.ret = list()

    def FindPath(self , root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        # method-1: DFS
        if not root:
            return []
        self.backtracking(root, target, [])
        return self.ret

    def backtracking(self, root, target, path):
        path.append(root.val)
        if root.val == target and not root.left and not root.right:
            self.ret.append(list(path)) # NOTE: remember to add list()!
            return
        if root.left:
            self.backtracking(root.left, target - root.val, path)
            path.pop()
        if root.right:
            self.backtracking(root.right, target - root.val, path)
            path.pop()