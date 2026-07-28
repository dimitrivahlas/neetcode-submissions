from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        #bfs from each treasure chest
        #to do this we need to find each treasure chest
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()

        def add_to_q(r,c):
            if (min(r,c) < 0 or r == rows or c == cols or (r,c) in seen or grid[r][c]==-1):
                return
            seen.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))

        
        dist = 0       
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                add_to_q(r+1,c)
                add_to_q(r-1,c)
                add_to_q(r,c+1)
                add_to_q(r,c-1)
            dist+=1
                    

        