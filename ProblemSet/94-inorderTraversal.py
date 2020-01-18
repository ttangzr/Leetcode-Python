'''
中序遍历
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _inorderTraversal(self, root, List):
        if root:
            self._inorderTraversal(root.left, List)
            List.append(root.val)
            self._inorderTraversal(root.right, List)
            
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        List = []
        if root == None:
            return List           
        
        self._inorderTraversal(root, List)

        return List
        
