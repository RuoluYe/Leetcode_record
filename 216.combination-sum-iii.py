#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = set()
        
        def helper(nums,n):
            for i in range(1,10):
                if i in nums:
                    continue
                if (n-i)==0 and (len(nums) == k-1):
                    nums.add(i)
                    if nums not in res:
                        res.append(nums.copy())
                    nums.pop()
                elif (n-i)>= 0:
                    nums.add(i)
                    helper(nums,n-i)
                    nums.pop()
                else:
                    break
        helper(nums,n)
        return res
# @lc code=end

def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = set()
        
        def helper(nums,n):
            for i in range(1,10):
                if i in nums:
                    continue
                if (n-i)==0 and (len(nums) == k-1):
                    nums.add(i)
                    if nums not in res:
                        res.append(nums.copy())
                    nums.pop()
                elif (n-i)>= 0:
                    nums.add(i)
                    helper(nums,n-i)
                    nums.pop()
                else:
                    break
        helper(nums,n)
        return res