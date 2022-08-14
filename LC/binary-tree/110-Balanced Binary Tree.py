# @Time    : 2020/6/27 9:21
# @Author  : T-
# @Site    : 
# @File    : 110-Balanced Binary Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # method-1: 自顶向下的递归
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

        # method-2: 自底向上的递归
        return height2(root) >= 0

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def height2(self, root):
        if not root:
            return 0
        leftHeight = self.height2(root.left)
        rightHeight = self.height2(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1



