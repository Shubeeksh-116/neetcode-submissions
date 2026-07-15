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
        

    #     class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     stack = [(p, q)]

    #     while stack:
    #         a, b = stack.pop()

    #         if not a and not b:
    #             continue

    #         if not a or not b or a.val != b.val:
    #             return False

    #         stack.append((a.left, b.left))
    #         stack.append((a.right, b.right))

    #     return True
