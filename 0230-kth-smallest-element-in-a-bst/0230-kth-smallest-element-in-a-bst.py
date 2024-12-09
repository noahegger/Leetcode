# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def rec(node):
            if node is None:
                return []
            
            return rec(node.left) + [node.val] + rec(node.right)

        return rec(root)[k-1]

            
            
            



        
