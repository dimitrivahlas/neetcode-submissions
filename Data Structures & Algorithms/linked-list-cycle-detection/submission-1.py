# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #just add every node to a set and check each time if its alreayd in there
        
        current = head
        visited = set()
        while head.next is not None:
            if current not in visited:
                visited.add(current)
            else:
                return True
            head = head.next
            current = head
        return False


