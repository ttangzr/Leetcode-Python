# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/08/07 11:20 PM

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.backtracking(1, n) if n else []
        
    def backtracking(self, start, end):
        if start > end:
            return [None]
        allTrees = []
        for i in range(start, end + 1):
            # 左子树都小于root
            leftTrees = self.backtracking(start, i - 1)
            # 右子树都大于root
            rightTrees = self.backtracking(i + 1, end)
            for l in leftTrees:
                for r in rightTrees:
                    currNode = TreeNode(i)
                    currNode.left = l
                    currNode.right = r
                    allTrees.append(currNode)
        return allTrees