class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # m = 0
        # for i in range(1, len(prices)):
        #     if prices[i]-prices[i-1]>0:
        #         m+=prices[i]-prices[i-1]
        
        # return m

        hold = -prices[0]
        cash = 0

        for p in prices[1:]:
            prev_hold, prev_cash = hold, cash
            
            hold = max(prev_hold, prev_cash-p)
            cash = max(prev_cash, prev_hold+p)
        
        return cash