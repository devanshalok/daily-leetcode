# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def subTree(root1,root2):

            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val!= root2.val:
                return False

            return subTree(root1.left,root2.right) and subTree(root1.right,root2.left)

        return subTree(root,root)

        