# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # floyd warshall algorithm 
        # make 2 pointers that start at the head and move one fast and one slow
        slow=head
        fast=head

        while fast and fast.next:
            # move the slow one only once
            slow=slow.next
            # move the fast twice 
            fast=fast.next.next

            # if there is a cycle the algo says that the pointers will definetly meet 
            # if they meet then there is cycle 
            if fast==slow:
                return True
        return False
        