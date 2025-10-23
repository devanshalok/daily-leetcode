class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # Preprocess the input to store all positions (indices) of each word.
        # Using a dictionary for O(1) lookup during queries.
        self.word_map = {}
        for index, word in enumerate(wordsDict):
            # Append the index to the list of that word.
            # If it's not in the map, create a new list.
            if word not in self.word_map:
                self.word_map[word] = []
            self.word_map[word].append(index)

        
    def shortest(self, word1: str, word2: str) -> int:
         # Retrieve the pre-stored index lists for both words.
        indices1 = self.word_map[word1]
        indices2 = self.word_map[word2]

        # Initialize pointers for both lists.
        i, j = 0, 0
        min_distance = float('inf')

        # Use two-pointer technique since both lists are sorted by construction.
        while i < len(indices1) and j < len(indices2):
            index1, index2 = indices1[i], indices2[j]
            # Update the minimum distance if the current pair is closer.
            min_distance = min(min_distance, abs(index1 - index2))

            # Move the pointer that points to the smaller index forward.
            # This helps us find potentially smaller differences.
            if index1 < index2:
                i += 1
            else:
                j += 1

        # Return the smallest distance found.
        return min_distance
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)