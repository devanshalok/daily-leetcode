class Solution(object):
    def twoSum(self, nums, target):
        temp={}

        for i,num in enumerate(nums):
            k=target-num

            if k in temp:
                return [temp[k],i]
            
            else:
                temp[num]=i
        