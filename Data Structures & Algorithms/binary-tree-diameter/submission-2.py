# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0

        def dia(node):
            nonlocal d
            if not node:
                return 0
            l = dia(node.left)
            r = dia(node.right)

            cur_dia = l + r

            if cur_dia>d:
                d = cur_dia
            
            return 1 + max(l,r)
        
        dia(root)
        return d
            