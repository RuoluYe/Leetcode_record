#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    class Difference:
        def __init__(self, nums) -> None:
            assert len(nums) > 0
            self.diff = [0]*len(nums)
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i]-nums[i-1]
        def increment(self, i, j, val):
            self.diff[i] += val
            self.diff[j+1] -= val
        def result(self):
            res = [0] * len(self.diff)
            res[0] = self.diff[0]
            for i in range(1, len(self.diff)):
                res[i] = res[i-1] + self.diff[i]
            return res
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = [0] * 1001
        df = self.Difference(nums)
        
        for trip in trips:
            val = trip[0]
            i = trip[1]
            j = trip[2]-1 # trip[2]时val已不在车上
            df.increment(i,j,val)
        res = df.result()
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        return True
            
# @lc code=end

