class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l_mult, r_mult = 1,1
        # Make a [0] array for left and right of the nums[] array
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)
        
        for i in range(len(nums)): 
            # Start from the left and right of the array and keep updating 
            # l_mult, r_mult by (nums*x_mult) and appending it to the l_arr,r_arr
            j = -i -1
            l_arr[i], r_arr[j] = l_mult, r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
            # after this loop the arrays will be [1,1,2,6] [24,12,4,1] <- test case 1
        
        # return the * of both the arrays merged in one array using Zip:
        # Zip basically makes pair of 2 same indexed array elements and make it one pair
        return [l*r for l, r in zip(l_arr, r_arr)]

































        