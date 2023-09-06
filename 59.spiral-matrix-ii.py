#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up, down = 0, n-1
        left, right = 0, n-1
        num = 1
        while num <= n*n:
            if up <= down:
                for i in range(left, right+1):
                    matrix[up][i] = num
                    num+=1
                up += 1
            if left <= right:
                for i in range(up, down+1):
                    matrix[i][right] = num
                    num+=1
                right -= 1
            if up <= down:
                for i in range(right, left-1, -1):
                    matrix[down][i] = num
                    num+=1
                down -= 1
            if left <= right:
                for i in range(down, up-1, -1):
                    matrix[i][left] = num
                    num+=1
                left += 1
        return matrix
# @lc code=end

