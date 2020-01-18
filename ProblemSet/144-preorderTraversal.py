'''
前序遍历
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _preorderTraversal(self, root, List):
        if root:
            List.append(root.val)
            self._preorderTraversal(root.left, List)
            self._preorderTraversal(root.right, List)
            
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        List = []
        if root == None:
            return List           
        
        self._preorderTraversal(root, List)

        return List
        
