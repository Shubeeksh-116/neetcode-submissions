class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        if len(s2)<len(s1):
            return False
            
        for s in s1:
            d1[s] = d1.get(s,0)+1
        
        for i in range(len(s1)):
            d2[s2[i]] = d2.get(s2[i],0)+1
        
        if d1==d2:
            return True

        l,r = 0,len(s1)-1
        print(d1)
        for i in range(len(s2)-len(s1)):
            
            print(d2)
            d2[s2[l]]-=1
            if d2[s2[l]]==0:
                d2.pop(s2[l])
            l+=1
            r+=1
            d2[s2[r]]+=1
            if d1==d2:
                return True
        
        return False
            

