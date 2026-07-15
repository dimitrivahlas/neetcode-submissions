class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #loop through and add to a hashmap, check hashmap and return true if any value is higher than 1
        #O(n)

        res = {}
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i],0)+1
            if res[nums[i]] > 1:
                return True
        return False  
