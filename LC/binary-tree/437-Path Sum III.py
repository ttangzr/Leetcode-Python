# @Time    : 2020/9/7 10:53
# @Author  : T-
# @Site    : 
# @File    : 437-Path Sum III.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # method-1:递归
        return self.dfs(root, targetSum, [])

        # method-2:双递归
        if not root:
            return 0
        return self.countPath(root, targetSum) + \
               self.pathSum(root.left, targetSum) + \
               self.pathSum(root.right, targetSum)

    def dfs(self, root, targetSum, sum_list):
        if not root:
            return 0
        # sum_list: [n1, n1+s1, ..., n1+sn], n1:root.val
        # update sum_list
        sum_list = [root.val + x for x in sum_list]
        # add root.val
        sum_list.append(root.val)
        # traversal
        count = 0
        for num in sum_list:
            if num == targetSum:
                count += 1
        return count + \
               self.dfs(root.left, targetSum, sum_list) + \
               self.dfs(root.right, targetSum, sum_list)

    def countPath(self, root, targetSum):
        # 以root为起点递归查找targetSum
        if not root:
            return 0
        count = 0
        if root.val == targetSum:
            count += 1
        left = self.countPath(root.left, targetSum - root.val)
        right = self.countPath(root.right, targetSum - root.val)
        return count + left + right

