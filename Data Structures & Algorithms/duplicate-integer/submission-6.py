class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for i in nums:
            dups.add(i)
        return len(dups) != len(nums)