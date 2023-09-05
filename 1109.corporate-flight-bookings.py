#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:
    class Difference:
        def __init__(self, nums: List[int]):
            assert len(nums) > 0
            self.diff = [0] * len(nums)
            # 根据初始数组构造差分数组
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i - 1]

    # 给闭区间 [i, j] 增加 val（可以是负数）
        def increment(self, i: int, j: int, val: int) -> None:
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val

    # 返回结果数组
        def result(self) -> List[int]:
            res = [0] * len(self.diff)
            # 根据差分数组构造结果数组
            res[0] = self.diff[0]
            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            return res
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        df = self.Difference(nums)
        for booking in bookings:
            i,j,val = booking[0]-1, booking[1]-1, booking[2]
            df.increment(i,j,val)
        return df.result()
        
# @lc code=end

