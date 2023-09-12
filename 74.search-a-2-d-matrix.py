#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        up, down = 0, rows-1
        while up <= down:
            row = (up+down)//2
            if target > matrix[row][-1]:
                up = row+1
            elif target < matrix[row][0]:
                down = row-1
            else: # target at this row
                break
        if not (up <= down):
            return False
        
        row = (up+down)//2 # declare with new up&down
        l, r = 0, cols - 1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] < target:
                l = m+1
            elif matrix[row][m] > target:
                r = m-1
            elif matrix[row][m] == target:
                return True
        return False
# @lc code=end

