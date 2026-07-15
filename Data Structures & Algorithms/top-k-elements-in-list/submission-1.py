class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i],0)+1
        
        res = []

        for n,c in counts.items():
            res.append([c,n])
        res.sort()

        result = []
        while len(result) < k:
            result.append(res.pop()[1])
        return result

        