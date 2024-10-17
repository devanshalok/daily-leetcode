class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We'll make an array of [1->max of the piles] to do binary search
        l=1
        r=max(piles)
        ans=r  

        while l<=r:
            # this is to do binary search on the made up array from above [1->max of the piles]
            hours=0
            m=(l+r)//2

            for p in piles:
                # calculate the total hours taken if koko eats mid number of bananas
                # every hour
                hours+=math.ceil(p/m)  

            # if these hours is more than the actual hours given than we'll move 
            # the left pointer to the mid cause we have to eat more bananas now in less time 
            if hours>h:
                l=m+1
            else:
                # if the hours is less than actual hours given more the right pointer 
                # towards mid , can be a answer but can find a better one thats why min of both
                ans=min(ans,m)
                r=m-1
             
        return ans


        