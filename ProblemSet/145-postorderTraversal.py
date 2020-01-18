'''
后序遍历
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _postorderTraversal(self, root, List):
        if root:
            self._postorderTraversal(root.left, List)
            self._postorderTraversal(root.right, List)
            List.append(root.val)
            
            
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        List = []
        if root == None:
            return List           
        
        self._postorderTraversal(root, List)

        return List
        
