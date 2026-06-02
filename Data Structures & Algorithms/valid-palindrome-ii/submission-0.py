class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[:]==s[::-1]:
            return True
        
        i,j = 0, len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            a = s[i+1:j+1]
            b = s[i:j]

            return a[:]==a[::-1] or b[:]==b[::-1]
        
        return True
