#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk = []
        visited = []
        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1
        for c in s:
            count[c] -= 1
            if c in visited:
                continue
            while stk and stk[-1] > c: # pop condition: new char c is smaller
                if count[stk[-1]] == 0: # if last char occurs no more, go ahead append c, so last char in stack
                    break
                visited.remove(stk.pop()) #else pop last char from stk,
            stk.append(c)
            visited.append(c)
        return "".join(stk)
# @lc code=end

