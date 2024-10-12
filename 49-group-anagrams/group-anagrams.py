class Solution(object):
    def groupAnagrams(self, strs):
        temp={}
        
        for s in strs:
            arr=[0]*26
            for l in s:    
                # takes every word from the string in the array and takes the 
                # difference from ASCII value of 'a' and adds it to the dict
                # eg: e -> e-a (70-65=5) so it adds 1 to i=5 in arr
                arr[ord(l)-ord('a')]+=1
            if tuple(arr) in temp:
                # if the array made from above is in temp's any key, 
                # append it in the value of the same key 
                temp[tuple(arr)].append(s)
            else:
                # else make a new value pair
                temp[tuple(arr)] = [s]
        #return the value of temp dict
        return temp.values()
        