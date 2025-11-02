class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros_count = 0
        max_len = 0

        for right in range(len(nums)):
            # If current element is 0, increment zeros count
            if nums[right] == 0:
                zeros_count += 1

            # If zeros exceed k, shrink window from left
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len