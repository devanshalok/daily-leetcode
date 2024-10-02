class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans=[]
        stack=[(0,0,[])]

        while stack:
            index,tar,can=stack.pop()

            if tar==target:
                ans.append(can)

            elif tar>target or index==len(candidates):
                continue
            
            else:
                stack.append((index, tar+candidates[index],can+[candidates[index]]))
                stack.append((index+1,tar,can))
        
        return ans

        