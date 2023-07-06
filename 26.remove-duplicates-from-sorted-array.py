#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l+1
# @lc code=end

