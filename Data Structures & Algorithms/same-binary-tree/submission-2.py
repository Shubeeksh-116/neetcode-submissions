# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(n):
            st = [n]
            out = []

            while st:
                x = st.pop()
                if x is None:
                    out.append(None)
                    continue
                out.append(x.val)

                st.append(x.right)
                st.append(x.left)

            return out

        return dfs(p)==dfs(q)              
        
