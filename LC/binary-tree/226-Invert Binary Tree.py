# @Time    : 2020/9/2 9:30
# @Author  : T-
# @Site    : 
# @File    : 226-Invert Binary Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # method-1:递归(DFS)
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

        # method-2: BFS（层次遍历）
        # 先将根节点放入到队列中，然后不断的迭代队列中的元素
        if not root:
            return None
        stack = [root]
        while stack:
            # 每次pop一个节点出来交换左右子节点
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

