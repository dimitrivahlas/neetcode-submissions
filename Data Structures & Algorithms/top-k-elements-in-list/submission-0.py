class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #intuition for this off the bat is, hash map with keys being different numbers 
        #of each value and then compare each key to each other 

        dic = {} 

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        return heapq.nlargest(k, dic.keys(), key=dic.get)
          