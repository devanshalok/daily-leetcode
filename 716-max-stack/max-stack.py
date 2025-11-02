from sortedcontainers import SortedDict

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MaxStack:
    def __init__(self):
        # Doubly linked list for stack order
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # SortedDict mapping value -> list of nodes with that value
        self.map = SortedDict()

    def _add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push(self, x: int) -> None:
        node = Node(x)
        self._add_node(node)
        if x not in self.map:
            self.map[x] = []
        self.map[x].append(node)

    def pop(self) -> int:
        node = self.tail.prev
        self._remove_node(node)
        self.map[node.val].pop()
        if not self.map[node.val]:
            del self.map[node.val]
        return node.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        return self.map.peekitem(-1)[0]  # largest key in SortedDict

    def popMax(self) -> int:
        max_val, nodes = self.map.peekitem(-1)
        node = nodes.pop()  # remove top-most node with max value
        self._remove_node(node)
        if not nodes:
            del self.map[max_val]
        return node.val
