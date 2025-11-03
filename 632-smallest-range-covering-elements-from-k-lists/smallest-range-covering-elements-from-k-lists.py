class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
         # Initialize a min-heap. Each entry is a tuple (value, list_index, element_index)
        heap = []
        current_max = float('-inf')

        # Step 1: Push the first element of each list into the heap
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))
            # Track the largest number among the first elements
            if val > current_max:
                current_max = val

        # Initialize best range as very large
        best_range = [float('-inf'), float('inf')]

        # Step 2: Keep processing until one list runs out of elements
        while True:
            # Get the smallest element (min_val)
            min_val, list_idx, elem_idx = heapq.heappop(heap)

            # Check if this range is smaller than the best found so far
            if (current_max - min_val < best_range[1] - best_range[0]) or \
               (current_max - min_val == best_range[1] - best_range[0] and min_val < best_range[0]):
                best_range = [min_val, current_max]

            # Move to the next element in the same list
            if elem_idx + 1 == len(nums[list_idx]):
                # We've reached the end of one list, so we can’t maintain a complete window anymore
                break

            # Get the next element from this list
            next_val = nums[list_idx][elem_idx + 1]
            # Push it into the heap
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            # Update the current maximum if needed
            if next_val > current_max:
                current_max = next_val

        return best_range