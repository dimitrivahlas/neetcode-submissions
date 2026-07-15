class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = {}
        
    
        for i in range(len(strs)):
            count = [0] * 26
            for c in strs[i]:
                count[ord(c) - ord("a")] +=1
            key = tuple(count)
            if key not in result:
                result[key] = []
                
            result[tuple(count)].append(strs[i])
        return list(result.values())
                