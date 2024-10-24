# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=head
        fast=head.next
        # This is done to find the middle point of the list 
        # the slow pointer will point to the middle of list
        # the fast pointer will be at the end of the list
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # this is to get the second half of the list 
        second=slow.next
        # the end of first half should be pointed to null
        # beacuse it always goes to the end 
        first=slow.next =None
        # This is to reverse the second half
        while second:
            temp=second.next
            second.next=first
            first=second
            second=temp

       # Merge the 2 lists
       # This line indicates the 2 ends of the list 
       # because after the 1st loop the 'first' pointer reaches the end of list
        first,second =head,first
        while second:
            temp1,temp2=first.next, second.next
            first.next=second
            second.next=temp1
            first, second=temp1, temp2

       