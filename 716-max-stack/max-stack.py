import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MaxStack:
    def __init__(self):
        # Create dummy head and tail for the doubly linked list
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Map value -> list of Node references (for duplicates)
        self.map = {}
        
        # Max heap to track max elements (negated for max behavior)
        self.max_heap = []
    
    def _addNode(self, node):
        # Add node at the end (right before tail)
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
    
    def _removeNode(self, node):
        # Remove node from linked list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def push(self, x):
        node = Node(x)
        self._addNode(node)
        
        # Add to hash map
        if x not in self.map:
            self.map[x] = []
        self.map[x].append(node)
        
        # Push to heap
        heapq.heappush(self.max_heap, -x)
    
    def pop(self):
        # Remove from end of list (top of stack)
        node = self.tail.prev
        self._removeNode(node)
        
        val = node.val
        self.map[val].pop()
        if not self.map[val]:
            del self.map[val]
        
        return val
    
    def top(self):
        # Return value of last node
        return self.tail.prev.val
    
    def peekMax(self):
        # Clean up heap for values no longer in the map
        while -self.max_heap[0] not in self.map:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0]
    
    def popMax(self):
        # Get current max
        max_val = self.peekMax()
        
        # Remove from heap
        node = self.map[max_val].pop()
        if not self.map[max_val]:
            del self.map[max_val]
        
        # Remove from linked list
        self._removeNode(node)
        
        return max_val
