from heapq import heappush, heappop, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heappush(maxHeap,[dist, x, y])
            if len(maxHeap) > k:
                heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heappop(maxHeap)
            res.append([x,y])
        return res



 