class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
       # Set because the array has duplicate numbers as well
       s=set(nums)
       long_seq=0

       for num in s:
        # check of its start of the sequence for this we check the previous number in the array
        if num-1 not in s:
            next_num=num+1
            length=1

            # loop through the array to see if the consequtive numbers are in the array
            while next_num in s:
                # update the length by 1 if the number is in the array
                length+=1
                next_num+=1
            long_seq=max(long_seq,length)

       return long_seq

    # INITIAL LOGIC THIS WILL RETURN ALL THE SEQ NOT THE LARGEST CONSECUTIVE

        # l=0
        # r=1
        # lar_seq=0
    
        # while r<len(nums) :
        #     if nums[r]-nums[l]==1:
        #         lar_seq+=1  

        #     l+=1
        #     r+=1 

        # if nums==[]:
        #     return lar_seq  
        # else:  
        #     return lar_seq+1   

        

        