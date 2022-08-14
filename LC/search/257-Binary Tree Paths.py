# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2021/12/24 8:54 AM

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._comb = list()
        self.combinations = list()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # method-1: backtracking
        self.backtracking(root)
        return self.combinations

    def backtracking(self, root):
        self._comb.append(str(root.val))
        if not root.left and not root.right:
            self.combinations.append("->".join(self._comb))
        if root.left:
            self.backtracking(root.left)
        if root.right:
            self.backtracking(root.right)
        self._comb.pop()


if __name__ == '__main__':
    obj = Solution()
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n5, n6)
    n3 = TreeNode(3)
    root = TreeNode(1, n2, n3)
    print(obj.binaryTreePaths(root))