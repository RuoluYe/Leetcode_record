#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start

# string manipulation
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.split()
        return len(ss[-1])

# @lc code=end

# pointer
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1,-1, -1):
            if s[i] != ' ':
                count += 1
            elif count > 0:
                return count
        return count
