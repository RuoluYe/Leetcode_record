#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get each char's freq
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num,0) +1
        freqs = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            freqs[freq].append(num)
        for i in range(len(freqs)-1, 0, -1):
            for j in freqs[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
# @lc code=end

priority queue
dictionary