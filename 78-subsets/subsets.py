class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        stack=[(0,[])]

        while stack:
            index,subset=stack.pop()

            if index==len(nums):
                ans.append(subset)
            
            else:
                stack.append((index+1,subset+[nums[index]]))
                stack.append((index+1,subset))

        return ans

    
    # class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:

    #     ans = []
    #     subset = []

    #     def dfs(n):
    #         if n == len(nums):
    #             ans.append(subset.copy())
    #             return
            
    #         subset.append(nums[n])
    #         dfs(n+1)
    #         subset.pop()
    #         dfs(n+1)
    #         return
            
            
    #     dfs(0)
    #     return ans
                


            


        
        