class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_addition = float("-inf")
        largest_current = 0

        for i in range(len(nums)):

            largest_current += nums[i]

            if largest_current >= largest_addition:
                largest_addition = largest_current
            
            if largest_current < 0:
                largest_current = 0
        
        return largest_addition
