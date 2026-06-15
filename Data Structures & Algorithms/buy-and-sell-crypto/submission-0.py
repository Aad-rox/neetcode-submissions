class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0

        
        for day in range(len(prices)-1,0, -1):

            minimum = min(prices[0:day])
            profit = prices[day]-minimum

            maxprofit = max(maxprofit, profit)

        return maxprofit