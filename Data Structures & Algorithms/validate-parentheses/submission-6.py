class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{", ")":"(", "]":"["}
        op = []
        for c in s:
            if c in d and len(op)<1:
                return False
            if c in d and op[-1]==d[c]:
                op.pop()
                continue
            op.append(c)
        if len(op)>0:
            return False
        return True