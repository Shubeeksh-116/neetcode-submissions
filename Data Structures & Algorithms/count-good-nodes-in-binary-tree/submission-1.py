# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0

        def x(n,h):
            nonlocal c

            if not n:
                return 
            
            if n.val>=h:
                c+=1
                h=n.val

            x(n.left,h)
            x(n.right,h)
        
        x(root,root.val)
        return c
