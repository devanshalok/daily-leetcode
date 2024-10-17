class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search indexing
        l,r=0,len(nums)-1

        while l<r:
            m=(l+r)//2
            # We will see if the mid number is greater than right number
            # it means that the right sorted portion is the one that
            # contains smaller elements and well move the left pointer 
            if nums[m]>nums[r]:
                l=m+1
            # else if the mid is smaller then the number is in the left sorted 
            # array move it to the mid
            else:
                r=m
        return nums[l]

        