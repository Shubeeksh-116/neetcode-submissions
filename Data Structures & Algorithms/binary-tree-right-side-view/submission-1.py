# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        out = []
        while q:
            this = []
            for i in range(len(q)):
                n = q.popleft()
                this.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            out.append(this)
        res = []
        for i in out:
            res.append(i[-1])
        return res