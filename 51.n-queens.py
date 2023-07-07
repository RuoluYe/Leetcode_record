#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        def backtrack(queenCol,leftDiagQ, rightDiagQ):
            if len(queenCol) == n:
                solutions.append(queenCol)
                return
            row = len(queenCol)
            for col in range(n):
                if (col not in queenCol and 
                    (row+col) not in leftDiagQ and
                    (row - col) not in rightDiagQ):
                    backtrack(queenCol+[col], leftDiagQ + [row+col], rightDiagQ + [row - col])

        backtrack([],[],[])
        # solution == [[1,3,0,2],[2,0,3,1]] possilbe col with Q
        
        # return [ ["." * i + "Q" + "." * (n-i-1) for i in sol] for sol in solution]
        res = []
        for sol in solutions:
            s = []
            for col in sol:
                s.append("." * col + "Q" + "." * (n-col-1))            
            res.append(s)
        return res
# @lc code=end

