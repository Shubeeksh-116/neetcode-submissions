class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = []
        for n in nums:
            heapq.heappush(x, n)
            if len(x)>k:
                heapq.heappop(x)
        
        return x[0]