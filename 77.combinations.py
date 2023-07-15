#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []
        def bt(n, start):
            if len(track) == k:
                res.append(track[:])
                return
            for i in range(start,n+1):
                track.append(i)
                bt(n,i+1)
                track.pop()
        bt(n, 1)
        return res
# @lc code=end

# Python library 
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))