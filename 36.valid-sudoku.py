#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numCols = [[] for i in range(len(board))] # numcols[i=1] = the number's occured columns
        # 0([0,0]-[2,2]), 1([0,3], [5,5]), 
        numBoxs = [[] for i in range(len(board))] 
        for r in range(len(board)):
            rowset = set()
            for i, num in enumerate(board[r]):
                if num == ".":
                    continue 
                if num in rowset:
                    return False
                rowset.add(i)
                
                numIndex = int(num)-1
                if i in numCols[numIndex]:
                    return False
                else:
                    numCols[numIndex].append(i)
                
                boxIndex = (r//3)+(i//3)
                if i in numBoxs[boxIndex]:
                    return False
                numBoxs[boxIndex].append(i)
        return True

                    
# @lc code=end

