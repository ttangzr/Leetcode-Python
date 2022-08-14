# @Time    : 2020/9/6 9:38
# @Author  : T-
# @Site    : 
# @File    : 617-Merge Two Binary Trees.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # method-1:递归 DLR
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


        # method-2: BFS
        if not root1:
            return root2
        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()
            if not node2:
                # node1一定不为None
                # 如果node2为空就不需要改动root1的数
                continue
            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
        return root1
