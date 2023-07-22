#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def getSum(n):
            res = 0
            while n > 0:
                res += (n%10)**2
                n = n//10
            return res
        while n not in seen:
            seen.add(n)
            n = getSum(n)
            if n == 1:
                return True
        return False
            
# @lc code=end

