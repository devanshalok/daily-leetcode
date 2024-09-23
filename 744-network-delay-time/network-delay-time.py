import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Use a regular dictionary to store edges
        edges = {}
        for u, v, w in times:
            if u not in edges:
                edges[u] = []  # Initialize the list if the key doesn't exist
            edges[u].append((v, w))

        # Min-heap to store (weight, node)
        minHeap = [(0, k)]
        # Set to keep track of visited nodes
        visit = set()
        # Variable to store the maximum time
        result = 0

        while minHeap:
            # Pop the smallest element from the heap
            w1, n1 = heapq.heappop(minHeap)
            # Skip if the node is already visited
            if n1 in visit:
                continue

            # Mark the node as visited
            visit.add(n1)
            # Update the result with the maximum weight
            result = max(result, w1)

            # Explore the neighbors of the current node
            if n1 in edges:
                for n2, w2 in edges[n1]:
                    if n2 not in visit:
                        heapq.heappush(minHeap, (w1 + w2, n2))

        # Check if all nodes are visited
        return result if len(visit) == n else -1
