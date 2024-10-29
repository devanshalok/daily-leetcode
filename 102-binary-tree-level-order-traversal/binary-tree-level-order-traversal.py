# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base Case if the root is NULL
        if root is None:
            return []
        # Make a queue and append the full tree to the queue
        queue=deque()
        queue.append(root)
        ans=[]
        
        while queue:
            # make an array to append the levels we extract from the tree
            level=[]
            n=len(queue)
            # extract nodes at each level of the tree
            for i in range(n):
                # pop the first node
                node=queue.popleft()
                # append the node's value to the level array
                level.append(node.val)
                # now append the left and right of the node just visited to the queue
                # the if part checks if the node exists or not
                if node.left: queue.append(node.left)                
                if node.right: queue.append(node.right)
            # append the level just extracted to the answer array (level is also an array)
            ans.append(level)

        return ans  