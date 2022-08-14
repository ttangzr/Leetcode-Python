# @Time    : 2020/6/24 11:03
# @Author  : T-
# @Site    : 
# @File    : 104-Maximum Depth of Binary Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # method-1: DFS递归
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

        # method-2: BFS（层次遍历）
        # 利用栈的思想，在DFS访问每个结点时，同时更新最大的深度
        # 从深度为1的栈开始，将当前结点弹出栈并对如子节点，每一步都更新深度
        if not root:
            return 0
        stack = deque([root])
        level = 0
        while stack:
            sz = len(stack)
            for _ in range(sz):
                node = stack.popleft()
                print(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            level += 1
        return level



