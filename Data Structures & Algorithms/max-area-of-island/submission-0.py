class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c): # each island we visit we add to set
            if (r < 0 or r == rows or c < 0 or
                c == cols or grid[r][c] == 0 or
                (r, c) in visited
            ):

                return 0
            
            visited.add((r,c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))
        size = 0

        for r in range(rows):
            for c in range(cols):
                size = max(size, dfs(r,c))
        return size
    
 