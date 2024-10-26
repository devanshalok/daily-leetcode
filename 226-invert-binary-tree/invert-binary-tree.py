# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case if there are no nodes in the tree
        if not root:
            return root
        # we just have root's left and right reversed 
        root.right,root.left=root.left,root.right
        # now recurse for every node of the tree
        # for every node we do this
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
        
        
        
        