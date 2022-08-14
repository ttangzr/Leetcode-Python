# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/26 8:51 AM
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
# @return int整型
#
class Solution:
    def __init__(self):
        self.cnt = 0

    def FindPath(self , root: TreeNode, sum: int) -> int:
        # write code here
        # method-1: backtracking
        if not root:
            return 0
        # backtracking每个节点
        self.backtracking(root, sum, [])
        self.FindPath(root.left, sum)
        self.FindPath(root.right, sum)
        return self.cnt

    def backtracking(self, root, target, path):
        if not root:
            return
        if root.val == target:
            # 满足时不要return
            self.cnt += 1
        self.backtracking(root.left, target - root.val, path)
        self.backtracking(root.right, target - root.val, path)
