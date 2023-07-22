#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            res = 0
            while n > 0:
                res += (n%10)**2
                n = n//10
            return res
        slow, fast = getSum(n) , getSum(getSum(n))
        while(slow!=fast):
            slow = getSum(slow)
            fast = getSum(getSum(fast))
        return slow == 1
            
# @lc code=end

