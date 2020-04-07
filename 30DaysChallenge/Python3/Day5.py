class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0 
        last_bought = float("inf")
        
        for price in prices:
            if price > last_bought:
                profit += price - last_bought
            last_bought = price
            
        return profit