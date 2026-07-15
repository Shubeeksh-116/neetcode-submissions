# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        d = deque([root])
        depth = 0
        res = []

        while d:
            l = len(d)
            res.append([node.val for node in d])

            for _ in range(l):
                n = d.popleft()
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
            
            depth +=1
        print(res)
        return depth