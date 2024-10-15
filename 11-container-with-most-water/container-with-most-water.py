class Solution(object):
    def maxArea(self, height):
        # Initialize the max area and the pointers
        max_area=0
        start=0
        end=len(height)-1

        while end>start:
            # compute the initial area starting at the min of the height of 2 pointers
            area = (end-start) * min(height[start],height[end])
            # in subsequent iterations update the area with the max of prev areas and current area
            max_area = max(area,max_area)
            # if the 2nd pointer height is more move the 1st pointer by 1
            if height[end]>height[start]:
                start+=1
            # else move the end pointer by 1 to the start
            else:
                end-=1
        return max_area


            

        
        