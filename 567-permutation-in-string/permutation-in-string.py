class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)
        temp1=[0]*26
        temp2=[0]*26

        # Base case if s1 length < s2 length
        if len(s2)<len(s1):
            return False
        # Till s1 keep inserting ord in both temp array (compare first two chars)_
        for i in range(len(s1)):
            temp1[ord(s1[i])-ord('a')]+=1
            temp2[ord(s2[i])-ord('a')]+=1

        # If both the temp arrays are true return true
        if temp1==temp2:
            return True

        # Keep sliding the window by 1 and adding the chars in window to the temp array, checking simultanously
        # if the s1 window has the chars in s2
        for i in range(len(s1),len(s2)):
            temp2[ord(s2[i])-ord('a')]+=1
            temp2[ord(s2[i-len(s1)])-ord('a')]-=1

            if temp1==temp2:
                return True
        # if none of this return true return false
        return False







        