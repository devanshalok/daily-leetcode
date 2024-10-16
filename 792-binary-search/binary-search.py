class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Make two pointer for sliding window 
        l,r=0,len(nums)-1

        while l<=r:
            # Get the mid of the array
            m=(l+r)//2

            # if the element is in the middle of the array return the index
            if nums[m]==target:
                return m

            # if the num in the middle is greater than target move the right 
            # pointer to mid-1
            if nums[m]>target:
                r=m-1
            
            # if the num in the middle is less than target move the left 
            # pointer to mid+1
            if nums[m]<target:
                l=m+1

        # If not found return -1
        return -1
            
             
        