class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        endOfArray =0
        
        for num in nums:
            if nums == 0:
                zeroes += 1
            else:
                nums[endOfArray] = num
                endOfArray += 1
                
        for _ in range(zeroes):
            nums[endOfArray] = 0
            endOfArray += 1
        