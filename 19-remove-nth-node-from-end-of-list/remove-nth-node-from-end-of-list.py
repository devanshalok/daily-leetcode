# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Make a dummy list node so that L and R can start from it 
        # the concept here is also of slow and fast pointer 
        dummy=ListNode()
        # attach is to the head of the list 
        dummy.next=head
        # initially the pointers are at the dummy node
        l=r=dummy

        # move the right pointer by the number of node to be deleted from end 
        while n>0:
            r=r.next
            n-=1
        # moving the right pointer by n nodes makes sure that when we start moving
        # the left pointer it reaches the .next of the node to be deleted
        while r.next:
            # this will move till the right.next is not null
            l=l.next
            r=r.next
            
        # this will break the connection from the previous node
        # and will attach that node to the next of the node to be deleted 
        l.next=l.next.next

        return dummy.next
    
        