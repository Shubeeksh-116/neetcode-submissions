class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l,r = 1,m
        op = m
        while l<=r:
            mid = (l+r)//2
            t = 0
            for p in piles:
                need = p//mid
                if p%mid>0:
                    need+=1
                t+=need
            if t<=h:
                op = mid
                r= mid-1
            else:
                l=mid+1
        return op
