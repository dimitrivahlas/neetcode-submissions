from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #maxheap of size k
        maxHeap = []
        for num in nums:
            heappush(maxHeap,num)
            if len(maxHeap) > k:
                heappop(maxHeap)

        return maxHeap[0]
        