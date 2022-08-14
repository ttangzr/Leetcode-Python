# -*- coding: utf-8 -*-
# @Author  : ZhirongTang
# @Time    : 2021/12/1 8:44 上午

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # method-1: backtracking / divide-and-conquer
        return self.generateSubtrees(1, n) if n else []

    def generateSubtrees(self, start, end):
        if start > end:
            return [None]
        allTrees = []
        for i in range(start, end + 1):     # root node
            leftTrees = self.generateSubtrees(start, i - 1)
            rightTrees = self.generateSubtrees(i + 1, end)
            for l in leftTrees:
                for r in rightTrees:
                    currNode = TreeNode(i)
                    currNode.left = l
                    currNode.right = r
                    allTrees.append(currNode)
        return allTrees

if __name__ == '__main__':
    obj = Solution()
    n = 3
    print(obj.generateTrees(n))
