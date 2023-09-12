#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for today, t in enumerate(temperatures):
            while stack and stack[-1][1] < t: # t is a warmer day
                day, temp = stack.pop()
                res[day] = today - day
            stack.append((today, t))
        return res
            
# @lc code=end

