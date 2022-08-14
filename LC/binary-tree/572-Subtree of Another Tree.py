# @Time    : 2020/9/15 9:08
# @Author  : T-
# @Site    : 
# @File    : 572-Subtree of Another Tree.py
# @Software: PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # method-1: 双递归
        if not s and not t:
            return True
        if not s or not t:
            return False
        else:
            # s为父二叉树，t为子二叉树，注意用or
            return self.isSameTree(s, t) \
                   or self.isSameTree(s.left, t) \
                   or self.isSameTree(s.right, t)

        # method-2: DFS+串匹配(暴力匹配, KMP, Rabin-Karp[注意负值])
        # KMP: https://blog.csdn.net/weixin_39561100/article/details/80822208
        # Rabin-Karp: https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode/

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            return s.val == t.val \
                   and self.isSameTree(s.left, t.left) \
                   and self.isSameTree(s.right, t.right)



