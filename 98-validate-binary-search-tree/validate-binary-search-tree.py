# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            # base case if there are no nodes in the tree
            if not node:
                return True
            # condition of binary tree-> the left side of the node should be
            # smaller and the right side should be grater than the entire node
            # if its not true return False
            if not (left < node.val < right):
                return False
            # now recursively call the subsequent nodes of the tree for the entire 
            # left and right subtree
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))

# Stack Approach 

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         stack=[(root,-math.inf,math.inf)]

#         while stack:
#             root,low,high=stack.pop()
#             if not root:
#                 continue

#             val=root.val
#             if val<=low or val>=high:
#                 return False
#             stack.append((root.right,val,high)) #setting the bounds cannot be smaller than val and can be infinite
#             stack.append((root.left,low,val))

#         return True
                

        


        
            
            

        
        