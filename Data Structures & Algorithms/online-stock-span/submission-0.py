class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        cur = 1
        while self.st and price >= self.st[-1][0]:
            p,s = self.st.pop()
            cur+=s
        self.st.append([price, cur])
        return cur


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)