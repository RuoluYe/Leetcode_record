#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:   
            res = 0
            if i == '+':
                res = stk.pop() + stk.pop()
                stk.append(res)
            elif i == '-': 
                a, b = stk.pop(), stk.pop()
                res = b - a
                stk.append(res)
            elif i == '*':
                res = stk.pop()*stk.pop()
                stk.append(res)
            elif i == '/':
                a, b = stk.pop(), stk.pop()
                res = int(b/a)
                stk.append(res)
            else:
                stk.append(int(i))
        return stk[-1]
# @lc code=end

