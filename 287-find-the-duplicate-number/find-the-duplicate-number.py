class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we will use slow and fast pointers here
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

        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return fast


        

        



       
        