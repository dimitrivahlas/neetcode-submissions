class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for i in strs:
            count = [0] * 26 #a...z

            for c in i:
                count[ord(c)- ord("a")]+= 1
            
            res[tuple(count)].append(i)
        return res.values()

                
        