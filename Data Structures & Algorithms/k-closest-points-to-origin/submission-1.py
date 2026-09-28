class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = []
        for i in points:
            d = math.sqrt((i[0]**2)+(i[1]**2))
            heapq.heappush(x, (d,[i[0],i[1]]))
        res = heapq.nsmallest(k,x)
        out = []
        for i in res:
            out.append(i[1])
        return out