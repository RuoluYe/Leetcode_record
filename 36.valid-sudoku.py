#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        colSet = [set() for i in range(len(board))] # numcols[i=1] = the number's occured columns
        # 0([0,0]-[2,2]), 1([0,3], [5,5]), 
        squares = collections.defaultdict(set) 
        rowSet = [set() for i in range(len(board))] 
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue 
                if (board[r][c] in rowSet[r]
                    or board[r][c] in colSet[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                colSet[c].add(board[r][c])
                rowSet[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

                    
# @lc code=end

