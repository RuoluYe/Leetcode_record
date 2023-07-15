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
                if i > start and nums[i] == nums[i-1]: # i > start! not i > 0
                    continue
                
                bt(curr+[nums[i]], i+1)
                
        
        bt([],0)       
        return res
# @lc code=end

确保每次for loop 遍历后面的nums，而不是从头遍历
for i in range(start, len(nums)): 
    
    if i > start and ...: # 因为 i = start时是新一层节点，不应跳过， 当i>start时还在该层，应跳过相同的数字