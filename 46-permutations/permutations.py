class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]       
        stack=[(nums, [])]  

        while stack:
            current_nums,current_path=stack.pop()  

            if not current_nums:
                result.append(current_path)  
            else:
                for i in range(len(current_nums)):
                    new_nums=current_nums[:i]+current_nums[i+1:] 
                    new_path=current_path+[current_nums[i]]  
                    stack.append((new_nums,new_path))  

        return result

        # def permute(self, nums: List[int]) -> List[List[int]]:

        # ans = []
        # cur = []

        # def backtrack():
        #     if len(cur) == len(nums):
        #         ans.append(cur.copy())
        #         return

        #     for i in nums:
        #         if i not in cur:
        #             cur.append(i)
        #             backtrack()
        #             cur.pop()
        # backtrack()
        # return ans

            

        



        