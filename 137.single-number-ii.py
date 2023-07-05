#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1 # num>>i 定位，&1 取值
            if count % 3: # if count%3 ==1, the number has 1 at bit position 1
                res |= (1 << i) # res or（1<<i), put 1 at the position i and maintain other bits. 
        return res 
# @lc code=end

# time complexity: 32n times, O(32n) = O(n)
# space complexity: O(1), no extra space