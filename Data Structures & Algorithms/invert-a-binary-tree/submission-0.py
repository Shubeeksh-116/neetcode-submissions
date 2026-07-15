# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        st = [root]

        while st:
            t = st.pop()
            t.left, t.right = t.right, t.left

            if t.left: 
                st.append(t.left)
            if t.right:
                st.append(t.right)

        return root