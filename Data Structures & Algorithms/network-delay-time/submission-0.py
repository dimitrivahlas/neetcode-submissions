class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #break this problem up into subproblems
        #we are given, times which is a list of directed edges
        #given times[i] = (ui, vi, ti) where ui is the source node
        #vi is the target node
        #ti is the time it takes for a signal to travel from the source to the target node

        #for constraints or rules we have: vi is an int from 1 to n, ui is int 1 to n, ti is int >= 0
        #given n directed nodes labeld 1 to n 

        #given k, which is the node that we will send a signal from
        #What were being asked for: min time it takes all n nodes to recieve the signal, else -1

        
        #this is a djikstras algorithm problem, shortest path graph algorithm

        #create adjacency list for djikstras algorithm
        edges = collections.defaultdict(list)

        for u,v ,w in times:
            edges[u].append((v,w))
        minHeap = [(0, k)]
        visit = set() #set to keep track so we dont cycle
        t = 0 
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)

            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+ w2,n2))
        return t if len(visit) == n else -1




