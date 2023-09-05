#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0]) # 长，宽
        if m == 0 or n == 0: return
        self.preSum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # the area from [0,0] to [i,j] = area from [i-1][j]+A[i][j-1]-A[i-1][j-1]+matrix[i-1][j-1]
                self.preSum[i][j] = self.preSum[i-1][j]+self.preSum[i][j-1]-self.preSum[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1]-self.preSum[row1][col2+1]-self.preSum[row2+1][col1]+self.preSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

