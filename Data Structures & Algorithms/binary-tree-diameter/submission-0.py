# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #lets think about this, basically were just asked to find the longest path which is going to be number of nodes -1
        #so what im thinking is we need to traverse the tree inOrder and then have a max function

        self.res = 0

        def inOrder(curr):
            if not curr: 
                return 0
        
            #left subtree
            left = inOrder(curr.left)
            ##right subtree
            right = inOrder(curr.right)

            self.res = max(self.res, left + right)
            return 1+ max(left, right)
        inOrder(root)
        return self.res
