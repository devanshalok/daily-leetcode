class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
         # Step 1: Build adjacency list
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}  # person → group (1 or -1)
        
        # Step 2: BFS to color each connected component
        for person in range(1, n + 1):
            if person not in color:
                queue = deque([person])
                color[person] = 1  # assign a group
                
                while queue:
                    cur = queue.popleft()
                    for nei in graph[cur]:
                        if nei not in color:
                            color[nei] = -color[cur]  # assign opposite group
                            queue.append(nei)
                        elif color[nei] == color[cur]:
                            return False  # same group conflict
        return True
