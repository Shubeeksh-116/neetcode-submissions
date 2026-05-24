class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        for c in s:
            d1[c] = 1 + d1.get(c, 0)
        
        for c in t:
            d2[c] = 1 + d2.get(c, 0)
        
        if d1==d2:
            return True
        return False