class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sub = nums[0]

        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[i]
            max_sub = max(current_sum,max_sub)
        return max_sub