class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        newS = ""
        

        
        index = 0
        while (index < len(word1) or index < len(word2)):
            if index < len(word1):
                newS += word1[index]
            if index < len(word2):
                newS += word2[index]
            index += 1
        return newS


        
        