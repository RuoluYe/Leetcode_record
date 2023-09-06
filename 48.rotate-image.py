#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in matrix:
            self.reverse(row)
    def reverse(self,arr):
        i,j = 0, len(arr)-1
        while i < j: 
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
# @lc code=end

