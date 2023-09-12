#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stk = [] # pair: (index, height)
        # calculate bar that cannot extend to the right
        for i, h in enumerate(heights):
            start = i 
            while stk and stk[-1][1] > h: #last height taller
                # pop the last height
                index, height = stk.pop()
                # calculate all past bar's (height*(i-index)) 
                maxA = max(maxA, height*(i-index))
                start = index 
            # exit while loop when meet bar height < h
            stk.append((start, h)) # bar[i] can extend to the index start
        # iterate stk, all bars can extend to the end right bar (i = len(height))
        for i, h in stk:
            maxA = max(maxA, h*(len(heights) - i))
        return maxA
# @lc code=end

