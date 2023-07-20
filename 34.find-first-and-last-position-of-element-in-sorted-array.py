#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) //2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right = mid - 1
        if left >= len(nums) or nums[left]!= target:
            return [-1,-1]
        
        leftbound,rightbound = left,left
        while rightbound < len(nums):
            if nums[rightbound] != target:
                break
            else:
                rightbound+=1
        return [leftbound,rightbound-1]
        
        
# @lc code=end

