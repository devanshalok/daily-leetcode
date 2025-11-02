import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # Min-heap to store tuples: (sum, index in nums1, index in nums2)
        heap = []
        result = []

        # Step 1: Initialize heap with pairs using the first element of nums2
        # Only need the first min(k, len(nums1)) elements to start
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # Step 2: Extract k smallest pairs from the heap
        while heap and len(result) < k:
            current_sum, i, j = heapq.heappop(heap)  # Get smallest sum pair
            result.append([nums1[i], nums2[j]])      # Add corresponding pair to result

            # Step 3: If there is a next element in nums2, push the new pair into the heap
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result

    # Example usage:
    # nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    # Output: [[1,2],[1,4],[1,6]]
