class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #brute force is to try every single sub array possible
        #dp is to memorize each result in an array or even a map
        #use kadanes alg
        #subarray means continous alg so potentialy sliding window

        currentMax = nums[0]
        curMin,curMax= 1,1
        for i in range(len(nums)):
            tmp = curMax * nums[i]
            curMax = max(nums[i]* curMax,curMin * nums[i], nums[i])
            curMin = min(tmp, nums[i]*curMin, nums[i])
            currentMax = max(currentMax,curMax)
        return currentMax

            