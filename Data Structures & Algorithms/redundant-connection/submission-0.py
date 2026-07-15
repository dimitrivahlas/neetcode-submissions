class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find, what are the two groups we will sort into
        #edges needed and edges not needed

 #mantain parent of every node in array
        par = [i for i in range(len(edges)+1)] #ith node -> parent(1 - n)
    
        rank = [1] * (len(edges)+1)

        def find(x):
            res = par[x]
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

           
        
        def union(x,y):
            p1,p2 = find(x), find(y) #finds aprents for x and y

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]