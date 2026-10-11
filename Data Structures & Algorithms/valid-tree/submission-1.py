class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #cycle detection
        adj_list = defaultdict(list)

        #undirected so add to both
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited= set()
        def dfs(node,parent):
            
            if node in visited:
                return False
            visited.add(node)   

            for n in adj_list[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            return True  
        

        return dfs(0,-1) and len(visited) == n
        

        
