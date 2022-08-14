# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/10 6:51 PM

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # method-1: DFS (preorder)
        def dfs(root, depth):
            if not root:
                return
            res[depth] = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        res = dict()
        dfs(root, 0)
        return list(res.values())

        # BFS
        if not root:
            return []
        from collections import deque
        stack = deque([root])
        res = []
        while stack:
            sz = len(stack)
            # 不断刷新val, 最后一次刷新即该层最右节点
            val = None
            for _ in range(sz):
                node = stack.popleft()
                val = node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(val)
        return res


if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(1)
    l2 = TreeNode(2)
    l5 = TreeNode(5)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    root.left, root.right = l2, l3
    l2.right, l3.right = l5, l4
    print(obj.rightSideView(root))
