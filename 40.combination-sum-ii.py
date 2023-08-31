#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        if not candidates:
            return 
        candidates.sort() 
        track = []
        trackSum = 0
        
        def helper(track, start, trackSum):
            if trackSum == target:
                    res.append(track[:])
                    return
            if trackSum > target:
                return
            for i in range(start, len(candidates)):
                # skip same number
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                track.append(candidates[i])
                print(track)
                trackSum += candidates[i]
                helper(track, i+1, trackSum)
                trackSum -= candidates[i]
                track.pop()
        helper(track, 0, trackSum)
        return res
                 
                
# @lc code=end

