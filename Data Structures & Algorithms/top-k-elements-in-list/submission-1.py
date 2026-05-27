class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n]=1+d.get(n,0)
        
        h = []
        for key,v in d.items():
            heapq.heappush(h,(-v,key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res