#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap, array num order
        codes = {}
        for s in strs:
            count = [0]*26
            for c in s:
                delta = ord(c) - ord('a')
                count[delta] += 1
            code = str(count)
            if code not in codes:
                codes[code] = []
            codes[code].append(s)
        return codes.values()
            
    
                
# @lc code=end

