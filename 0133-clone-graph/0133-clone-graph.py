"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        otn_map = {}

        def clone(node):
            if node in otn_map:
                return otn_map[node]
            
            node_copy = Node(node.val)

            otn_map[node] = node_copy

            for n in node.neighbors:
                node_copy.neighbors.append(clone(n))

            return node_copy
        
        return clone(node) if node else None



















        # old_new_map = {}

        # def clone(node):
        #     if node in old_new_map:
        #         return old_new_map[node]

        #     copy = Node(node.val)
        #     old_new_map[node] = copy
            
        #     for nei in node.neighbors:
        #         copy.neighbors.append(clone(nei))
            
        #     return copy
        
        # return clone(node) if node else None

