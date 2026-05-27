class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out+=str(len(s))+"#"+s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i<len(s):
            l = ""
            while s[i]!="#":
                l+=s[i]
                i+=1
            lenn = int(l)
            out.append(s[i+1:i+lenn+1])
            i=i+lenn+1
        
        return out
        
