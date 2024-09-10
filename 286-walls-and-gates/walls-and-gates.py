class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows,columns=len(rooms),len(rooms[0])
        visit=set()
        q=deque()

        def addRooms(r,c):
            if r<0 or r==rows or c<0 or c==columns or (r,c) in visit or rooms[r][c]==-1:
                return 
            visit.add((r,c))
            q.append([r,c])

        for i in range(rows):
            for j in range(columns):
                if rooms[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))

        dist=0
        while q:
            for i in range(len(q)):
                r,c= q.popleft()
                rooms[r][c]=dist
                addRooms(r+1,c)
                addRooms(r-1,c)
                addRooms(r,c+1)
                addRooms(r,c-1)
            dist+=1
            

        