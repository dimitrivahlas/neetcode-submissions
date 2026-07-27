class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        mapping = defaultdict(int)

        for src, dst in trust:
            mapping[src] -=1
            mapping[dst] +=1

        for i in range(1,n+1):
            if mapping[i] == n -1:
                return i
        return -1




