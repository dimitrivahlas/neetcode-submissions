class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #is this sorted?
        #brute force is loop through and try each thing but that takes to long O(n^2)

        #instead we can use a hash map and check something different


        check ={}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in check:
                return [check[diff],i]
            check[nums[i]] = i
        return []