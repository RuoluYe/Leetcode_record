#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0,0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l 

# @lc code=end

