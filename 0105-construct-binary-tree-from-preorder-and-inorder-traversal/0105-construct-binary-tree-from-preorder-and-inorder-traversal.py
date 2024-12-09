# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

  #      left branch  x  right branch
        # inorder = [9, 3, 15, 20, 7]

    #                x
      # preorder = [ 3, 9, 20, 15, 7] # potential nodes    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        # find index in inorder list
        # left is left tree, right is right tree
        root_index = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])

        return root

        

        





        

