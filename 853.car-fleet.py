#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        pair = [[p,s] for p,s in zip(position, speed)] #list comprehension
        for p,s in sorted(pair)[::-1]:# position closer first
            time = (target-p)/s
            # first one, alway append
            # when stk >= 1, compare time with last time, 
            # if new time is faster, means they will become a fleet
            # if new time is slower(time>stack[-1]), add new time and it makes a fleet
            if len(stk) == 0 or (len(stk) >= 1 and time > stk[-1]):
                stk.append(time)
            
        return len(stk)
# @lc code=end

