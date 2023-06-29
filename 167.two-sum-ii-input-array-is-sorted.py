#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # double pointer
        left, right = 0, len(numbers)-1
        while left < right:
            n = numbers[left] + numbers[right]
            if n == target:
                return [left+1, right+1] #return 1-based-index
            if n < target:
                left += 1
            if n > target:
                right -= 1
        return []

# @lc code=end

