# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #slightly unoptimal solution and then optimize from there
        h = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            heapq.heappush(h,node.val)
            inorder(node.right)
        inorder(root)
        for i in range(k):
            k_th_smallest = heapq.heappop(h)
        return k_th_smallest
        



        