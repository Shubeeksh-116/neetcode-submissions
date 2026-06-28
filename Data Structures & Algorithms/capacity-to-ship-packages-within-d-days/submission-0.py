class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        op = r

        while l<=r:
            mid = (l+r)//2
            udays=1
            c = 0
            for w in weights:
                if c+w>mid:
                    udays+=1
                    c=0
                c+=w
            if udays<=days:
                op=mid
                r=mid-1
            else:
                l=mid+1
        
        return op