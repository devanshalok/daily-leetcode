class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        for i, num in enumerate(nums):
            if num == target:
                if res[0] == -1:
                    res[0] = res[1] = i
                else:
                    res[1] = i

        return res