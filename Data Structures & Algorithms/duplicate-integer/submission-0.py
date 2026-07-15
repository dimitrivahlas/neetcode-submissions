class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for n in range(len(nums)):
            for i in range(n +1, len(nums)):
                if nums[n] == nums[i]:
                    return True
                
        return False
         