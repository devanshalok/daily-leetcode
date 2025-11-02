# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find candidate
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                # Candidate knows i -> candidate cannot be celebrity
                candidate = i
            # else: candidate does not know i -> i cannot be celebrity

        # Step 2: Verify candidate
        for i in range(n):
            if i == candidate:
                continue
            # Celebrity does not know anyone
            if knows(candidate, i):
                return -1
            # Everyone must know celebrity
            if not knows(i, candidate):
                return -1

        return candidate
