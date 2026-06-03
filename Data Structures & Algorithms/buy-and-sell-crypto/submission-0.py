class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        p = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>m:
                m=prices[i]
                continue
            if m-prices[i]>p:
                p=m-prices[i]
        return p