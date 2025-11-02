class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Step 1: Initialize binary search boundaries
        left, right = 0, len(arr) - k  # The window of size k must fit within the array
        
        # Step 2: Binary search to find the left boundary of the k-element window
        while left < right:
            mid = (left + right) // 2
            # Compare distances of arr[mid] and arr[mid + k] from x
            # If arr[mid + k] is closer to x, move the window to the right
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid  # Else, we can keep the window starting at mid
        
        # Step 3: Slice the array from the found left index to get k elements
        return arr[left:left + k]

    # Example usage:
    # arr = [1,2,3,4,5], k = 4, x = 3
    # Output: [1,2,3,4]
