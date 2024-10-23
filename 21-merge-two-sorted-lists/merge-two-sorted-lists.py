# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we make a new link list to append the merged lists
        dummy=ListNode()
        tail=dummy

        # Loop through till the both lists are True
        while list1 and list2:
            # if list2 val is greater than list1 val append list1 to tail 
            if list2.val>=list1.val:
                tail.next=list1
                # move the tail pointer to the next of the list
                tail=tail.next
                # Move the list1 pointe rto the next of the list
                list1=list1.next

            else:
                # if list1 val is greater than list2 val 
                # follow same but for list2 now
                tail.next=list2
                tail=tail.next
                list2=list2.next

        # if after appending the equal number if elements some elements are left 
        # in either of the leist we append them as it is
        if list1:
            tail.next=list1

        if list2:
            tail.next=list2

        return (dummy.next)


        