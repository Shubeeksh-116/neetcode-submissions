class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = []

        d = {"2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def x(i, c):
            if i==len(digits):
                res.append(c)
                return 
            
            for l in d[digits[i]]:
                x(i+1,c+l)
        
        x(0,"")
        return res

