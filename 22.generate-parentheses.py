#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []
        res = []
        def bt(open, close):
            if open == close and open == n:
                res.append("".join(stk))
                return 
            if open < n:
                stk.append('(')
                bt(open+1, close)
                stk.pop()
            if close < open:
                stk.append(')')
                bt(open, close+1)
                stk.pop()
        bt(0,0)
        return res
# @lc code=end

