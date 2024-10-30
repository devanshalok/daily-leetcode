# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # make a stack for the nodes 
        stack=[]
        curr=root
        
        # we check if the stack is empty or we reach the end if tree
        # (i.e the node is null)
        while curr or stack:
            # loop to append all the nodes in the stack 
            # we only append the left side because of the smallest element 
            while curr:
                stack.append(curr)
                curr=curr.left

            # pop the element till kth iteration
            curr=stack.pop()
            k-=1

            if k==0:
                return curr.val
            # if not in the left side go to the right
            curr=curr.right

        
        