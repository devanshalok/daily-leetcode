class Solution(object):
    def containsDuplicate(self, nums):
        temp=set() #make a set cause in set you cannot have duplicate values

        # then start adding it in the set if it is in the set return False

        for i in nums:
            if i in temp:
                return True
            else:
                temp.add(i)
        return False
       
        
    
        