# @Time    : 2020/9/7 11:18
# @Author  : T-
# @Site    : 
# @File    : 113-Path Sum II.py
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        res = []

        def dfs(root, stack, sum_):
            sum_ += root.val
            if not root.left and not root.right:
                if sum_ == sum:
                    res.append(stack[:] + [root.val])
            elif not root.left:
                dfs(root.right, stack + [root.val], sum_)
            elif not root.right:
                dfs(root.left, stack + [root.val], sum_)
            else:
                dfs(root.left, stack + [root.val], sum_)
                dfs(root.right, stack + [root.val], sum_)

        dfs(root, [], 0)
        return res


        
if __name__ == "__main__":
    l1 = []
    l1.append([1, 2, 3] + [4])
    print(l1)
