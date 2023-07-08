#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = 0
    def totalNQueens(self, n: int) -> int:
        def backtrack(queensCol, leftDiag, rightDiag):
            if len(queensCol) == n:
                self.res += 1
                return
            row = len(queensCol)
            for col in range(n):
                if (not col in queensCol and 
                not (row+col) in leftDiag and 
                not (row-col) in rightDiag):
                    backtrack(queensCol+[col], leftDiag+[row+col], rightDiag+[row-col])

        backtrack([],[],[])
        return self.res
# @lc code=end

