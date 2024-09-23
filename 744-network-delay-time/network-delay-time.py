class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges=defaultdict(list)
        for u,v,w in times:
            if u not in edges:
                edges[u]=[]
            edges[u].append((v,w))
            

        minHeap=[(0,k)]
        heapq.heapify(minHeap)
        visit=set()
        result=0

        while minHeap:
            w1,n1 =heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            result=max(result,w1)

            if n1 in edges:
                for n2, w2 in edges[n1]:
                    if n2 not in visit:
                        heapq.heappush(minHeap, (w1 + w2, n2))
        
        return result if len(visit)==n else -1        