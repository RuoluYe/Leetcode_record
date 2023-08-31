#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxP = 0
        start = 0
        
        for i in range(len(nums)):
            product = nums[i]
            maxP = max(maxP, product)
            if i+1 == len(nums):
                return maxP
            for j in range(i+1, len(nums)):
                product *= nums[j]
                maxP = max(maxP, product)
        return maxP
                
            
            
            
# @lc code=end

