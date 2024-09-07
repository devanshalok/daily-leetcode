class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        g=defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)

        unvisited,visiting,visited=0,1,2
        states=[unvisited]*numCourses

        def dfs(i):
            if states[i]==visiting: return False
            if states[i]==visited: return True

            states[i]=visiting

            for n in g[i]:
                if not dfs(n):
                    return False

            states[i]=visited
            order.append(i)
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
            
        
        
        