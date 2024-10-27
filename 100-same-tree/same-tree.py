# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case if no nodes
        if not p and not q:
            return True
        
        # check if the 2 trees have same node and the values are equal
        if not p or not q or p.val!=q.val:
            return False
        # recursively call the function on the left and right of the tree for both of the trees
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        