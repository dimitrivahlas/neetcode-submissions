from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()    
        q = deque()
        def addRoom(r,c):
            if (r < 0 or r== len(grid) or c < 0 or c == len(grid[0]) or (r,c) in seen or grid[r][c] == -1):
                return
            seen.add((r,c))
            q.append([r,c])
        #find coordinates to bfs from
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1
        