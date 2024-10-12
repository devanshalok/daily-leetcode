class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums) #Counter in built lib creates the freq counter of all elements
        # Create a heap of most freq occureed elements 
        #(heap is min heap by default) that's why the -ve value for freq
        c=[(-v,k) for k,v in c.items()]
        heapq.heapify(c)

        output=[]

        for i in range(k):
            # Just pop the top k nodes in the heap and append the value to output
            item=heapq.heappop(c)
            output.append(item[1])

        return output
     
           
        