class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)

        unvisited=0
        visiting=1
        visited=2
        states=[unvisited]*numCourses
        
        def dfs(node):
            state=states[node]
            if state== visited: return True
            elif state==visiting: return False

            states[node]=visiting

            for n in g[node]:
                if not dfs(n):
                    return False
            states[node]=visited
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        

        
        
        