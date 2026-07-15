class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        res = 0

        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            res=max(res, dic[s[r]])

            if(r - l +1) - res > k:
                dic[s[l]] -= 1
                l += 1
        return (r - l +1)
            
