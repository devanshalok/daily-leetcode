class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res,prevEnd=len(points), points[0][1]

        for i in range(1, len(points)):
            curr=points[i]
            if curr[0]<=prevEnd:
                res-=1
                prevEnd=min(curr[1],prevEnd)
            else:
                prevEnd=curr[1]

        return res