class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0                 # left pointer for the sliding window
        zeros = 0                # count of zeros in the current window
        max_len = 0              # store the maximum window length found

        # expand the window by moving 'right' pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1       # count zeros as we expand the window

            # if we have more than k zeros, shrink window from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1   # one zero removed from the window
                left += 1        # move left pointer to shrink window

            # update maximum length of valid window
            max_len = max(max_len, right - left + 1)

        return max_len
            
        