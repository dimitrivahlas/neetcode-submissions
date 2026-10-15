class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []
        res = []
        def dfs(i):
            if i > n:
                if len(current) == k:
                    res.append(current.copy())
                return

            #add the current number
            current.append(i)
            dfs(i+1)

            current.pop()
            dfs(i+1)
        dfs(1)
        return res
