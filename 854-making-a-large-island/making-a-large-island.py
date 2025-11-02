class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        self.size[xr] += self.size[yr]


class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n * n)

        def index(r, c):
            return r * n + c

        # Step 1: Union all 1s
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            dsu.union(index(r, c), index(nr, nc))

        # Step 2: Compute island sizes
        area = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    root = dsu.find(index(r, c))
                    area[root] = dsu.size[root]

        max_area = max(area.values(), default=0)

        # Step 3: Try flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            seen.add(dsu.find(index(nr, nc)))
                    new_area = 1 + sum(area[root] for root in seen)
                    max_area = max(max_area, new_area)

        return max_area
