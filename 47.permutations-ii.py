#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums) # 记录用过的index
        def bt(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            # 每次从头来，否则range（start，len（nums））会跳过没用过的数
            for i in range(len(nums)):
                # 跳过用过的数！元素不可复选
                if used[i]:
                    continue
                # not used[i-1] 保证相同元素在排列中的相对位置不变，从而剪枝重复组合
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    # 如果前一个相同的数没被选择，则跳过
                    continue
                
                used[i] = True
                bt(cur+[nums[i]])
                used[i] = False
        bt([])
        return res
            

# @lc code=end
