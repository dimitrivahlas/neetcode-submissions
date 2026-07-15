class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #this question is asking, given a dictionary of strings
        #and a string s, can we split the string s into the words in the dict
        #in other words, can we actually find substrings of s that = dict[i]

        #or can we go the other way, can we start at list[0] and check if it is equal to any of the strings
        
        #dynamicaly store result if true in another dict
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if((i+len(w)) <= len(s) and s[i:i+len(w)] == w):
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)

      
            