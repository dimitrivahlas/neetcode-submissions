class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #think about what needs to be confirmed to be an anagram, we need to have the exact same length between both strings
        # we also need to have the exact same amount of each letter in each string
        #so we can loop through and add it to a map and then return true if both maps have the same amoiunt

        count1 = {}
        count2 = {}
        #base case of checking if they are diff lenght
        if len(s) != len(t):
            return False
        
        #since we get past the first base case we can assume we have the same length strings at this point
        
        for i in range(len(s)):
            a = s[i]
            count1[a] = count1.get(a, 0)+1
            b = t[i]
            count2[b] = count2.get(b,0)+1
        
       
        return count1 == count2
