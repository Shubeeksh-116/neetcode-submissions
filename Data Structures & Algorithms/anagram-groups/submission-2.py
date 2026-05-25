class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            t = [0]*26
            for c in s:
                t[ord(c)-ord("a")]+=1
            res[tuple(t)].append(s)
        
        return list(res.values())