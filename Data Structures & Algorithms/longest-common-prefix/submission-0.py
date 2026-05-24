class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = float("inf")

        for s in strs:
            if len(s)<l:
                l = len(s)
        
        out = ""

        for i in range(l):
            t = strs[0][i]
            c = 0
            for s in strs:
                if s[i]==t:
                    c+=1
            if c==len(strs):
                out+=t
            else:
                break
                
        
        return out




