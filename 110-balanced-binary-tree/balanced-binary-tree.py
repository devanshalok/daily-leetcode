# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True

        def dfs(root):
            # base case
            if not root:
                return True

            # calculate the left and right height of the tree
            left=dfs(root.left)
            right=dfs(root.right)

            # check if the height is greater than 1 (question's req)
            if abs(left-right)>1:
                self.balanced=False
            # return the height of the tree
            return 1+max(left,right)
        
        dfs(root)
        return self.balanced

        