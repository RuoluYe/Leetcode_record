#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], [] #quad to keep track of current quaduple
        
        def nSum(n, start, target): # n = how many, start = index
            if n != 2: # not base case
                for i in range(start, len(nums) - n + 1): # e.g. when n = 4, use len(nums) - 3, make sure there are 3 other numbers left to form a quaduple
                    if nums[i] == nums[i-1] and i > start: # skip same number after nums[i]
                        # i > 0 might skip current number, would not pass 4sum([2,2,2,2,2], 8) 
                        continue
                    quad.append(nums[i])
                    nSum(n-1,i+1,target-nums[i]) # recursion to get (n-1)Sum
                    quad.pop() 
                
            else: # now quad is [a, b], needs two more
                l,r = start, len(nums) -1

                while l < r:
                    if nums[l] + nums[r] < target: #or nums[l] == nums[l-1]？
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad+[nums[l], nums[r]])
                        l += 1 # update pointer otherwise while loop would not stop
                        while l < r and nums[l] == nums[l-1]:
                            l += 1 # skip same number after nums[l]
                        
        
        nSum(4, 0, target)
        return res            


            
# @lc code=end


# 1. sort input
# helper function nSum(n, starting index, left target)
# quad append current nums[i], pass nSum(n-1, i+1, target - nums[i])
# 2. break down problem to looking for 2 sum and use 2 pointers

    