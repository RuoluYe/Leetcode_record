#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in nums:
                if i in track:
                    continue
                # track.append(i)
                # backtrack(track)
                # track.pop()
                backtrack(track+[i])
        backtrack([])
        return res
                
# @lc code=end

for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    # 判断
    如果选择 in 路径: continue
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择再加入选择列表
