#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        up,down,left,right = 0,m-1,0,n-1
        res = []
        while len(res) < m*n: # m*n is the result[] length
            if up <= down:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up+=1
            if left <= right:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right-=1
            if up <= down:
                for i in range(right,left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
        
# @lc code=end

