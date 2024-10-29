# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # initialize the good nodes
        nums=0
        # make a stack for the node and a value to compare that node's value 
        stack=[(root,-math.inf)]
        # run the loop till stack is empty
        while stack:
            # pop the top element of the stack 
            node,maxNode=stack.pop()

            # if the value of the node is greater than the value of the stack 
            # increase the nums by 1
            if node.val>=maxNode:
                nums+=1

            # after this append the left and right of the node to the stack 
            # append the max of the current maxNode and value of that node
            if node.left:
                stack.append((node.left,max(node.val,maxNode)))

            if node.right:
                stack.append((node.right,max(node.val,maxNode)))

        return nums

        