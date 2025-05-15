# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case if there is no root in the tree
        if not root:
            return 0
        # now we just calculate recirsively the depth of the left side
        # and the right side of the tree and store it in 2 variables
        left=self.maxDepth(root.left) 
        right=self.maxDepth(root.right)
        
        # return the max of left and right and add 1 for the root
        return 1+max(left,right)




        