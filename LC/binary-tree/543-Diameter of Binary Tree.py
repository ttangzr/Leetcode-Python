# @Time    : 2020/8/11 11:33
# @Author  : T-
# @Site    : 
# @File    : 543-Diameter of Binary Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
        
    def diameterOfBinaryTree(self, root: TreeNode):
        # method-1: DFS
        # 转换为求以各个节点为起点，经过的最多节点数（包括L和R）的最大值-1即为直径
        self.ans = 1
        self.depth(root)
        return self.ans - 1

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        # 可不穿过根节点
        self.ans = max(self.ans, left + right + 1)
        return max(left, right) + 1

    
