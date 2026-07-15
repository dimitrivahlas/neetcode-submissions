class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        path = set() # no duplicates

        def dfs(r, c, i): #r is row c is column, i is current letter were lloking for
            if i == len(word):
                return True
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False

            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or #check all 4 adjacnet positions
                    dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
                    
        return False
            

