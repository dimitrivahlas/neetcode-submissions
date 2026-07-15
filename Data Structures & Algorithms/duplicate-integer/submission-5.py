class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #add each value into a set
        s = set()

        for i in range(len(nums)):
            s.add(nums[i])
        
        if len(s) != len(nums):
            return True
        return False