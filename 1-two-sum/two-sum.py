class Solution(object):
    def twoSum(self, nums, target):
        #dict stores the {number:index} key-value pair
        temp={}

        for i,num in enumerate(nums): #enumerate keeps track of the index while iterating
            k=target-num #temp variable updates with the diff of target and number at current index
            if k in temp:
                #if k in temp dict return the value of key and the i
                return [temp[k],i]
            else:
                #else add the pair to the dict
                temp[num]=i