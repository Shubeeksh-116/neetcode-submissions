# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0

        def dfs(n, g):
            nonlocal c

            if not n:
                return
            if n.val>=g:
                c+=1
                
            
            dfs(n.left, max(n.val,g))
            dfs(n.right,max(n.val,g))
        
        dfs(root,root.val)
        return c
