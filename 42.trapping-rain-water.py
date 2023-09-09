#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        maxl, maxr = [0]*n, [0]*n
        maxl[0], maxr[-1]  = height[0], height[-1]
        for i in range(1,n):
            maxl[i] = max(maxl[i-1], height[i])
        for i in range (n-2, -1, -1):
            maxr[i] = max(height[i], maxr[i+1])
        for i in range(1,n-1):
            res += min(maxl[i],maxr[i])- height[i]
        return res
# @lc code=end

