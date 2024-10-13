class Solution(object):
    def twoSum(self, numbers, target):
        start= 0
        end= len(numbers)-1

        # sliding window in which only one pointer moves
        while end>=start:
            # if conditions to see if 2Sum is larger than target
            if numbers[start]+numbers[end]>target:
                end-=1

            # if conditions to see if 2Sum is smaller than target
            if numbers[start]+numbers[end]<target:
                start+=1

            # if conditions to see if 2Sum is equal to target
            if numbers[start]+numbers[end]==target:
                break
        
        return [start+1,end+1]
        