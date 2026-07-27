"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        mapping = {}

        def clone(node):
            #could be in multiple lists 
            if node in mapping:
                return mapping[node] 
           
            new_node = Node(node.val)
            mapping[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(clone(n))
            
            return mapping[node]
        return clone(node)


            
        