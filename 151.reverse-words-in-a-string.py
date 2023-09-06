#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        return " ".join(s)
# @lc code=end

