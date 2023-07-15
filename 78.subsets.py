#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        def backtrack(nums, start):
            res.append(list(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop()
        backtrack(nums,0)
        return res
# @lc code=end

def subsets(self, nums):
    res = [[]]
    for n in nums:
        for i in range(len(res)):
            res.append(res[i] + [n])
    return res