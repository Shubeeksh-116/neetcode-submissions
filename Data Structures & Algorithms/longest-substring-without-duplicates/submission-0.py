class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        i,j = 0,0
        m = 0

        for j in range(len(s)):
            d[s[j]] = d.get(s[j],0)+1

            if d[s[j]]>1:
                while d[s[j]]>1:
                    d[s[i]] = d[s[i]]-1
                    i+=1
            
            if (j-i+1)>m: m = j-i+1
        
        return m