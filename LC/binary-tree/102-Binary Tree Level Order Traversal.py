# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/24 21:41

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = deque([root])
        while stack:
            sz = len(stack)
            res_ = []
            while sz:
                node = stack.popleft()
                res_.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                sz -= 1
            res.append(res_)
        return res