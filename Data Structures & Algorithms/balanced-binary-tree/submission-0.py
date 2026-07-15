# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        out = True

        def x(n):
            nonlocal out
            if not n:
                return 0
            
            l = x(n.left)
            r = x(n.right)

            if abs(l-r)>1: 
                out = False

            return 1 + max(l,r)
        
        x(root)
        return out
