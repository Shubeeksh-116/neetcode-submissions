# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        dia = 0

        def x(n):
            nonlocal dia
            if not n:
                return 0
            r = x(n.right)
            l = x(n.left)
            dia = max(dia, l+r)
            return 1 + max(l,r)
        
        x(root)
        return dia