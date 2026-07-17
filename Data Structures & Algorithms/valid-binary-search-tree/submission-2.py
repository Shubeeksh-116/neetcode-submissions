# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(n, l, r):
            if not n:
                return True
            if n.val<r and l<n.val:
                return dfs(n.left, l, n.val) and dfs(n.right, n.val, r)
            else:
                return False

        return dfs(root, -float("inf"), float("inf"))