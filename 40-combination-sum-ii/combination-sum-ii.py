class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer=[]
        stack=[(0,0,[])]

        while stack:
            index,tar,ans=stack.pop()

            if tar==target:
                answer.append(ans)

            elif tar>target or index==len(candidates):
                continue

            else:
                stack.append((index+1, tar+candidates[index],ans+[candidates[index]]))

                while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                    index+=1
                
                stack.append((index+1,tar,ans))

        return answer
        