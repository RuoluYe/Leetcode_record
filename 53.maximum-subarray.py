#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for i in nums:
            if curSum < 0:
                curSum = 0 #如果上一个sum < 0, 则归零
            curSum += i # add after compare b/c only adding to positive sums
            maxSum = max(curSum, maxSum)
        return maxSum
# @lc code=end


