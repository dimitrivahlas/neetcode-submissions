class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        counts1 = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0 )+1
            counts1[t[i]] = counts1.get(t[i],0)+1
        
        return counts1 == counts