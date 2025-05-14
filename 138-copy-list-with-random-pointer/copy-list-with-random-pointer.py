"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):

        curr=head
        newdict={None:None}

        # To copy the node and teh next of the node 
        while curr:
            node=Node(x=curr.val)
            newdict[curr]=node
            curr=curr.next

        curr=head

        # To copy the random pointer 
        while curr:
            newnode=newdict[curr]
            newnode.next=newdict[curr.next] 
            newnode.random=newdict[curr.random] 
            curr=curr.next

        return newdict[head]

        