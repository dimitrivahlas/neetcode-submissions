class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax,globmin = nums[0],nums[0]

        curMax =0
        curMin = 0
        total = 0

        for n in nums:
            curMax = max(curMax +n,n)
            curMin = min(curMin +n,n)
            total += n
            globmax = max(globmax, curMax)
            globmin = min(globmin,curMin)
        
        return max(globmax,total-globmin) if globmax > 0 else globmax