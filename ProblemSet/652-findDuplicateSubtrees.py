''''
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        # method-1
        d = collections.defaultdict(list)
        def dfs(root):
            if not root: return ''
            s = ' '.join((str(root.val), dfs(root.left), dfs(root.right)))
            d[s].append(root)
            return s
        dfs(root)
        return [l[0] for l in d.values() if len(l) > 1]

	# # method-2
	# def findDuplicateSubtrees(self, root):
	# 	ans = []
	# 	d = collections.defaultdict(list)
	# 	def dfs(root):
	# 		if not root: 
	# 			return ' '
    #     	s = ' '.join((str(root.val) + dfs(root.left), dfs(root.right)))
    #     	if s not in d:
	# 			d[s] = True
    #     	elif d[s]:
	# 			ans.append(root)
    #             d[s] = False
    #     	return s
	# 	dfs(root)
	# 	return ans
            
        