import random

class RandomizedSet:
    def __init__(self):
        # List to store elements
        self.arr = []
        # Map value -> index in arr
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        # Append to list
        self.arr.append(val)
        # Store index in hashmap
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        # Get index of element to remove
        idx = self.pos[val]
        # Swap with last element
        last_val = self.arr[-1]
        self.arr[idx] = last_val
        self.pos[last_val] = idx
        # Remove last element
        self.arr.pop()
        # Remove from hashmap
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.arr)
