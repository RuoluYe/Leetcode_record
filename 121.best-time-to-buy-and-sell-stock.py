#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for price in prices[1:]:
            lowest = min(lowest, price)
            profit = max(price - lowest, profit)
        return profit
# @lc code=end

