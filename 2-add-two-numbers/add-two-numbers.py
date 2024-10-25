# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
    # Make a dummy node to move the pointer
        dummy=ListNode()
        curr=dummy
        carry=0

        # we have to keep on adding till either one of the list is empty 
        # or the carry that we have is not 0
        while l1 or l2 or carry:
            # extract the first values from both the lists
            # if either of the list is valu is not present we put v(x)=0
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            # we sum the values and also heres a carry from the additon 
            # of values before if the have any (carry is 0 initially)
            sum=v1+v2+carry
            # carry is extracted by // by 10 cause this gives out the
            # remainder and it is the extra digit if its greater than 10
            carry=sum//10
            # this gives out the actual sum that is to be appended to the new list
            # this is teh qoutient of the sum
            sum=sum%10
            # append the sum to the new list made above 
            curr.next=ListNode(sum)
            # move the pointer to the next of the new list
            curr= curr.next
            # move the lists pointer to the next node and if none 
            # move the pointer to None
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next






    