#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if coin <= i: # trim negative results
                    dp[i] = min(dp[i], dp[i-coin] +1 ) # = (child + 1) coins
        if dp[amount] == (amount+1):
            return -1
        else:
            return dp[amount]
        
     
# @lc code=end

# identify base case, condition, choice


#自顶向下，暴力
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return -1
#         res = float('inf')
#         for coin in coins:
#             sub = self.coinChange(coins, amount - coin)
#             if sub == -1:
#                 continue
#             res = min(res, sub+1) # 1 + min(coinChange(coins, amount - coin)) = coins amount
#         return res if res!=float('inf') else -1