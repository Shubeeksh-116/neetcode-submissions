class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        a = self.d[key]
        l,r = 0, len(a)-1
        res = ""

        while l<=r:
            mid = (l+r) // 2

            if a[mid][0]<=timestamp:
                res = a[mid][1]
                l = mid+1
            else:
                r = mid-1
        
        return res