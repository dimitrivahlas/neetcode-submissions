class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        

        while left <= right:
            mid = left + (right - left) // 2
            midval = nums[mid]
            if midval == target:
                return mid
            elif target < midval:
                right = mid - 1
            else:
                left = mid + 1

        return -1

        

        