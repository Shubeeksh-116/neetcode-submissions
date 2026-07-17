# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        st = [root]
        while st:
            n = st.pop()
            if n.val==p.val or n.val==q.val:
                return n
            elif p.val<n.val<q.val or p.val>n.val>q.val:
                return n
            elif p.val<n.val and q.val<n.val:
                st.append(n.left)
            else:
                st.append(n.right)
        
