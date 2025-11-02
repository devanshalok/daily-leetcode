class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # Initialize positions of word1 and word2 to -1 (meaning not seen yet)
        index1, index2 = -1, -1
        # Initialize minimum distance to a large number
        min_dist = float('inf')
        
        # Iterate through the array once
        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i  # Update the latest index of word1
                # If word2 has been seen, update min_dist
                if index2 != -1:
                    min_dist = min(min_dist, abs(index1 - index2))
            elif word == word2:
                index2 = i  # Update the latest index of word2
                # If word1 has been seen, update min_dist
                if index1 != -1:
                    min_dist = min(min_dist, abs(index1 - index2))
        
        return min_dist  # Return the shortest distance found

    # Example usage:
    # wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    # word1 = "coding", word2 = "practice"
    # Output: 3
