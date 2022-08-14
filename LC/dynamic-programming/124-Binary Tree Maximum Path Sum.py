# -*- coding: utf-8 -*-
# @Author  : Zhirong Tang
# @Time    : 2022/3/9 9:45 PM
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # method-1: DP
        self.maxGain(root)
        return self.maxSum

    def maxGain(self, node):
        if not node:
            return 0
        # 递归计算左右子节点的最大贡献
        left_gain = max(self.maxGain(node.left), 0)
        right_gain = max(self.maxGain(node.right), 0)
        # 节点最大路径取决于该节点和左右子节点的最大贡献
        node_gain = node.val + left_gain + right_gain
        # 更新最大路径和
        self.maxSum = max(self.maxSum, node_gain)
        # 节点最大贡献（最大上升路径和）
        return node.val + max(left_gain, right_gain)

