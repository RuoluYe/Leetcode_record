#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def bt(curr, start):
            res.append(curr[:])
            for i in range(start, len(nums)): # start, otherwise memory limit exceed
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                
                bt(curr+[nums[i]], i+1)
                
        
        bt([],0)       
        return res
# @lc code=end

