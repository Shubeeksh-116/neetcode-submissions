class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def x(i, j, c):
            if len(c)==2*n:
                res.append(c[:])
                return

            if i<n:
                c=c+"("
                x(i+1,j,c)
                c=c[:-1]
            
            if j<i:
                c=c+")"
                x(i,j+1,c)
                c=c[:-1]

        
        x(0,0,"")
        return res