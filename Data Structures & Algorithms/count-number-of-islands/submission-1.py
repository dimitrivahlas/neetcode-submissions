class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
           #dfs from every one, unless marked
        res = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(i, c):
            if(i < 0 or c < 0 or i >= len(grid) or c >= len(grid[0]) or grid[i][c] == "0" ):
                return
            #if these dont occur, run the dfs
            grid[i][c] = "0"
            for dr, dc in directions:
                dfs(i + dr, c + dc)

        for i in range(len(grid)):
            for c in range(len(grid[0])): 
                if grid[i][c] == '1':
                        dfs(i,c)
                        res += 1
        
        return res
            
                       
       