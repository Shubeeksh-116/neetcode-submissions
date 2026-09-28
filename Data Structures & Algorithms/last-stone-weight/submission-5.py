class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = []
        for s in stones:
            heapq.heappush(a, -s)
        
        while len(a)>=2:
            x = -heapq.heappop(a)
            y = -heapq.heappop(a)
            if x!=y:
                heapq.heappush(a, -abs(x-y))
        
        if len(a)==0:
            return 0
        return -a[0]