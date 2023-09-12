#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]: # the array is sorted
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # a part of the left sorted, 
                # search right sorted
                l = m+1
            else: # m < l, search left sorted portion
                r = m-1  
        return res
# @lc code=end

