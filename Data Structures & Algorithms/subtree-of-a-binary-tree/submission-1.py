# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(x):
            st = [x]
            out = []

            while st:
                n = st.pop()
                if n is None:
                    out.append(None)
                    continue
                out.append(n.val)
                
                st.append(n.right)
                st.append(n.left)
            
            return out
        
        s = [root]
        while s:
            n = s.pop()
            if n.val == subRoot.val:
                if dfs(n) == dfs(subRoot):
                    return True
            if n.right: s.append(n.right)
            if n.left: s.append(n.left)

        return False