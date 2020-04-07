class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Kadane's Algorithm"""
        best = -float("inf")
        
        running = 0
        for num in nums:
            running += num
            best = max(running, best)
            running = max(0 ,running)
        
        return best
            
        
        
        