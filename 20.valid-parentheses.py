#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(",
               "]":"[",
               "}":"{"}
        stk = []
        for i in s:
            if i not in Map.keys(): #( [, {}
                stk.append(i)
                continue
            if not stk or stk[-1] != Map[i]:
                return False
            stk.pop()
        return not stk
# @lc code=end

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        left = ['(', '[', '{']
        right = [')', ']','}']
        for i in s:

            if i in left:
                stk.append(i)
            elif not stk or stk[-1] not in left:
                return False
            elif i in right:
                last = stk.pop()
                if ((i == ')' and last != '(')
                or (i == ']' and last != '[' )
                or (i == '}' and last != '{')):
                    return False
        return len(stk) == 0
                