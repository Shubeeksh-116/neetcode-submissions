class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1,k
        out = k
        while l<=r:
            k = (l+r)//2
            hn = 0
            for i in range(len(piles)):
                if piles[i]%k!=0:
                    hn+=(piles[i]//k)+1
                else:
                    hn+=(piles[i]//k)
            if hn <= h:
                out = k
                r=k-1
            else:
                l=k+1
        return out
            

