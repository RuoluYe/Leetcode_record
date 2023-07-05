#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXorb = 0
        for i in nums:
            aXorb ^= i
        last = aXorb & (-aXorb)  # bit where a and b differs
        a = 0
        for i in nums:
            if ((last & i) != 0): # check if number has 1 at that bit position
                a ^= i # first group will be left with number a
        return [a, aXorb^a] # b = aXorb ^ a
# @lc code=end

# first run ^ to get the a^b
# search the position to do partitioning in binary representation of a^b
# partition the array by this position and get a and b correspondingly
# e.g. [1,2,1,3,2,5]

# 1 = 001
# 2 = 010
# 1 = 001
# 3 = 011
# 2 = 010
# 5 = 101

# after 1st step, we found out that a^b = 3^5 = 6 which is 110
# 110 means that there are 2 digits on the left are different in binary representation of our result
# let's use any one of the digit to partition our array

# if we use the middle one, we can see that there are 2 sets of numbers that we can just use the simple single number to find out the single in each partition
# 1 = 001
# 1 = 001
# 5 = 101 ✅
# 2 = 010
# 2 = 010
# 3 = 011 ✅

# if we use the leftmost one, we can still partition the array into the sets and do simple single number on it
# 1 = 001
# 2 = 010
# 1 = 001
# 3 = 011✅
# 2 = 010
