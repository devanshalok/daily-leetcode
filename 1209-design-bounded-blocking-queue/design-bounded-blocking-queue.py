import threading

class BoundedBlockingQueue:
    def __init__(self, capacity):
        # Initialize queue storage and capacity
        self.queue = []
        self.capacity = capacity
        
        # A lock ensures mutual exclusion for queue operations
        self.lock = threading.Lock()
        
        # Two condition variables:
        # 'not_full' to block producers when queue is full
        # 'not_empty' to block consumers when queue is empty
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, element):
        with self.not_full:  # Acquire lock via condition
            # While queue is full, block producer until consumer signals space
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            
            # Append new element at the front (as per problem)
            self.queue.insert(0, element)
            
            # Signal that queue now has at least one element
            self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:  # Acquire lock via condition
            # While queue is empty, block consumer until producer signals item
            while len(self.queue) == 0:
                self.not_empty.wait()
            
            # Remove element from rear of queue
            value = self.queue.pop()
            
            # Signal that queue now has space for more elements
            self.not_full.notify()
            
            return value

    def size(self):
        with self.lock:  # Just need mutual exclusion to read safely
            return len(self.queue)
