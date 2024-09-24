class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price=[float("inf")]*n
        price[src]=0

        for i in range(k+1):
            tmpPrices= price.copy()

            for source,destination,money in flights:
                if price[source]+money<tmpPrices[destination]:
                    tmpPrices[destination]=price[source]+money

            price=tmpPrices
        
        return -1 if price[dst]==float("inf") else price[dst]

