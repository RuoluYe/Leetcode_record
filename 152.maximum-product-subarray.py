#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmp = curMax *n
            curMax = max(n*curMax, n*curMin, n) # dp: keep the current max and min
            curMin = min(tmp, n*curMin, n)
            res = max(res, curMax)
        
        return res
    
         
# @lc code=end
