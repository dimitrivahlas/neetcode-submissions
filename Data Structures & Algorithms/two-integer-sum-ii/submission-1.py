class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #i believe we just add each number until we get over the target
        #returning as an array
        l = 0
        r = len(numbers) -1

        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else: 
                return [l+1, r+1]
        return []


