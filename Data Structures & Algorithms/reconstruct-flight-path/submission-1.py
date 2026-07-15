class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #create adjacency list
        adjacencyList = {from_i : [] for from_i, to_i in tickets}
        tickets.sort()
        for from_i, to_i in tickets:
            adjacencyList[from_i].append(to_i)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1: 
                return True
            if src not in adjacencyList:
                return False
            
            temp = list(adjacencyList[src])
            for i, v in enumerate(temp):
                adjacencyList[src].pop(i)
                res.append(v)
                
                if dfs(v): return True
                adjacencyList[src].insert(i,v)
                res.pop()
            
            return False
        dfs("JFK")
        return res