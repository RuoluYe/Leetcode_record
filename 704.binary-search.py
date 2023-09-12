#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            i = left + (right - left) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                left = i+1.
            else:
                right = i-1
        return -1
                
# @lc code=end

