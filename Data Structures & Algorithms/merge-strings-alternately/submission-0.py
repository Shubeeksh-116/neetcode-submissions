class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        w1,w2 = len(word1), len(word2)
        i,j = 0,0
        while i<w1 and j<w2:
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        
        res+=word1[i:]
        res+=word2[j:]
        return res
        
