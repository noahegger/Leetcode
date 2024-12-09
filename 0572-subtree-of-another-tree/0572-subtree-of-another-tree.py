# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(r, s):
            if not r and not s:
                return True
            
            if not r or not s:
                return False

            return r.val == s.val and isIdentical(r.left, s.left) and isIdentical(r.right, s.right)

        if not root:
            return False

        if isIdentical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)