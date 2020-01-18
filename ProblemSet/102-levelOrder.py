'''
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _levelOrder(self, root, level, List):
        if root:
            if len(List) < level + 1:
                List.append([])
            List[level].append(root.val)
            self._levelOrder(root.left, level + 1, List)
            self._levelOrder(root.right, level + 1, List)


    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        List = []
        if root == None:
            return List           
        
        self._levelOrder(root, 0, List)

        return List
        