#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def longest(s:str,i:int):
            seen = set()
            for ch in range(i,len(s)):
                if s[ch] in seen: # should examine s[ch], not ch(the index).
                    return len(seen)
                seen.add(s[ch])
            return len(seen)
        
        res = 0
        for i in range(len(s)):
            res = max(res, longest(s,i))
        return res
                    
# @lc code=end

