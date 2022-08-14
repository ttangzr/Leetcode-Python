# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/2/23 6:55 PM
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param proot TreeNode类
# @param k int整型
# @return int整型
#
class Solution:
    def __init__(self):
        self.count = 0
        self.ret = -1

    def KthNode(self , proot: TreeNode, k: int) -> int:
        # write code here
        # method-1: DFS
        if not proot or k <= 0:
            return -1
        self.KthNode(proot.left, k)
        self.count += 1
        if self.count == k:
            self.ret = proot.val
            return self.ret
        self.KthNode(proot.right, k)
        return self.ret

        # method-1: BFS
        if not proot or k <= 0:
            return -1
        count = 0
        stack = list()
        curr = proot
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            ret = curr.val
            if count == k:
                return ret
            curr = curr.right
        return -1
