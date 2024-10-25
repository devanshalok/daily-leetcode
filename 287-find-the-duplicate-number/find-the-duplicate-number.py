class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we will use slow and fast pointers here
        # its basically detecting a loop in the list 
        slow=nums[0]
        fast=nums[0]

        while nums:
            # the condition of the question satisfies we can use 
            # the number for indexes 
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break

        slow=nums[0]

        # Run the loop again till slow and fast pointer comes to the loop
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return fast


        

        



       
        