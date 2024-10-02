class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]
        stack=[(0,[])]

        while stack:

            index,ans=stack.pop()

            if index==len(nums):
                answer.append(ans)

            else:
                stack.append((index+1, ans+[nums[index]]))
                while index+1<len(nums) and nums[index]==nums[index+1]: 
                    index+=1
                stack.append((index+1, ans))

        return answer  