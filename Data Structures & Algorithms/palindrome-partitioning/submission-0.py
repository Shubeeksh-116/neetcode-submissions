class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def is_pal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l +=1
                r-=1
            return True

        def x(i,c):
            if i==len(s):
                res.append(c[:])
                return
            
            for j in range(i, len(s)):
                if is_pal(i,j):
                    c.append(s[i:j+1])
                    x(j+1, c)
                    c.pop()
            
        x(0,[])
        return res
            
            