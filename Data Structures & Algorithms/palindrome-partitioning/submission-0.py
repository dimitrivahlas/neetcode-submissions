class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #go through decision tree and add if palindrome, false if not
        res = [] 
        part = [] # current parittion

        def dfs(i):
            if i >= len(s): #base case
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                #evvery possible substrinug so now we check if palindrome
                if self.isPali(s,i,j): #check from index i to index j
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
                
        dfs(0)
        return res
    def isPali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l+1, r-1
        return True