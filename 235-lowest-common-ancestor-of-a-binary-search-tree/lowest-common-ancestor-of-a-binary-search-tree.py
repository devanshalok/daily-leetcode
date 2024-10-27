# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # binary search tree is where left side is smaller then the root 
        # and right side is greater than the root
        while root:
            # the root is the ancestor of every node in the tree
            # so we check from the root and move downwards

            # we keep pn moving downwards from the root 
            # depending on the value of the nodes given 

            if p.val>root.val and q.val>root.val:
                root=root.right

            elif p.val<root.val and q.val<root.val:
                root=root.left

            else:
                return root
        