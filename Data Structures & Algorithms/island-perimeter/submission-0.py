class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    
        #find the island then count all edges that touch either water or the side
        count = 0            
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                #find the island
                if grid[r][c] == 1:
                    count += (r + 1 >= rows or grid[r+1][c] == 0)
                    count += (c + 1 >= cols or grid[r][c+1] == 0)
                    count += (r - 1 < 0 or grid[r-1][c] == 0)
                    count += (c - 1 < 0 or grid[r][c-1] == 0)
        return count
                    