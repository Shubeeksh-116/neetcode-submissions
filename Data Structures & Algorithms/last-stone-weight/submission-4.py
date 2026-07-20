class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []
        for s in stones:
            print(self.heap)
            heapq.heappush(self.heap, -s)

        while len(self.heap)>1:
            a = -heapq.heappop(self.heap)
            b = -heapq.heappop(self.heap)
            if a==b:
                continue
            elif a>b:
                heapq.heappush(self.heap, -(a-b))
            else:
                heapq.peappush(self.heap, -(b-a))
        
        if len(self.heap)==1:
            return -self.heap[0]
        return 0