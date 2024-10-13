class Solution(object):
    def isPalindrome(self, s):
        # create a sliding window 
        start=0
        end=len(s)-1

        # compare each alpha numeric characrter in the sliding window (s[0]:s[-1])
        while end>start:
            #check if the character is alpha-num, if not continue
            if not(s[start].isalnum()):
                start+=1
                continue
            if not(s[end].isalnum()):
                end-=1
                continue
            # If one character mimatches return False, else True
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1

        return True


        
            

       