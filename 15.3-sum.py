#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: #check if same number as the index before
                continue
            l, r = (i + 1), len(nums) -1
            while l < r:
                sum = a + nums[l] + nums[r] # - target， target = 0
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -=  1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1 # check next b
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                
                
# @lc code=end

