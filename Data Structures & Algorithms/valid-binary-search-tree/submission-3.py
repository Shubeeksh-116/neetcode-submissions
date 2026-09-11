# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out = True

        def dfs(n, mi, ma):
            nonlocal out
            if not n:
                return
            if n.val<=mi or n.val>=ma:
                out = False
                return
            dfs(n.left, mi, n.val)
            dfs(n.right, n.val, ma)
        
        dfs(root, -float('inf'), float('inf'))
        return out