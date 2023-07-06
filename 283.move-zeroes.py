#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0,0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        # l is on the exclusive end of all non-zero 
        while l < len(nums):
            nums[l] = 0
            l += 1
        return nums
                
# @lc code=end

