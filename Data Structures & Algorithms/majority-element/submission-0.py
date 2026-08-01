class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)   
        res =  max_count = 0 
        for n in nums:
            freq[n] += 1
            if max_count < freq[n]:
                res =n
                max_count = freq[n]
        return res
            
        
